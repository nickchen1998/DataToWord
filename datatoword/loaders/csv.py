from . import BaseLoader
import csv
from io import StringIO
from typing import List
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage


class CSVLoader(BaseLoader):
    def create_documents(
            self,
            file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 1000
    ) -> List[Document]:
        documents = []
        for row in self.parse_binary_content(file_binary_content):
            if not row or row[0].replace(" ", "") == "":
                continue

            messages = self.generate_messages(file_name, file_description, row)
            ai_message = self.llm.invoke(messages)
            if "這是標頭" in ai_message.content:
                continue

            document = Document(page_content=ai_message.content)
            if metadata:
                document.metadata = metadata
            documents.append(document)

        return documents

    def parse_binary_content(self, file_binary_content: bytes) -> list:
        try:
            content_str = file_binary_content.decode('utf-8')
            csv_reader = csv.reader(StringIO(content_str))
            return list(csv_reader)
        except csv.Error as e:
            raise ValueError("無效的 CSV 內容") from e

    def generate_messages(self, file_name: str, file_description: str, row: list) -> List[BaseMessage]:
        system_message = """
        你是一個 CSV 專家，請根據我提供給你的檔案描述，以及檔案名稱，將我給你的資料轉換成一個 300 字以內的敘述，
        並同時參考下列條件：
        1. 請使用繁體中文
        2. 如果你判斷給你的資料為標頭，請回傳 "這是標頭"。
        ----------------
        參考範例：
        
        檔案名稱：地球大學學生資料表.csv
        檔案描述：這是一個學生資料表，包含了學生的姓名、學號、性別、年齡等資訊。
        轉換前資料：nick, 1998, men, 23
        轉換後資料：在地球大學中，有一位名叫 nick 的男性學生，他的學號是 1998，年齡是 23 歲。
        """

        human_message = """
        檔案名稱：{file_name}
        檔案描述：{file_description}
        轉換前資料：{row}
        """.format(file_name=file_name, file_description=file_description, row=row)

        return [
            SystemMessage(system_message),
            HumanMessage(human_message)
        ]

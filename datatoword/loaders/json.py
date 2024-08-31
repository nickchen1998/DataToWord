import json
from . import BaseLoader
from langchain_core.documents import Document
from typing import List, Union
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage


class JSONLoader(BaseLoader):

    def create_documents(
            self, file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 300
    ) -> List[Document]:
        json_content = json.loads(file_binary_content.decode('utf-8'))
        if isinstance(json_content, list):
            datas = json_content
        else:
            splitter = RecursiveJsonSplitter(max_chunk_size=chunk_size)
            datas = splitter.split_json(json_data=json_content)

        return self._generate_documents(file_name, file_description, datas, metadata)

    def parse_binary_content(self, file_binary_content: bytes):
        try:
            return json.loads(file_binary_content.decode('utf-8'))
        except json.JSONDecodeError as e:
            raise ValueError("無效的 JSON 內容") from e

    def generate_messages(self, file_name: str, file_description: str, data: Union[list, dict]) -> List[BaseMessage]:
        system_message = """
            你是一個 JSON 專家，請根據我提供給你的檔案描述，以及檔案名稱，將我給你的資料轉換成一個 300 字以內的敘述，
            並同時參考下列條件：
            1. 請使用繁體中文
            ----------------
            參考範例：
    
            檔案名稱：地球大學學生資料表.json
            檔案描述：這是一個學生資料表，包含了學生的姓名、學號、性別、年齡等資訊。
            轉換前資料：{"name": "nick", "number": 1998, "gender": "meal", "age": 23}。
            轉換後資料：在地球大學中，有一位名叫 nick 的男性學生，他的學號是 1998，年齡是 23 歲。
        """

        human_message = """
            檔案名稱：{file_name}
            檔案描述：{file_description}
            轉換前資料：{data}
        """.format(file_name=file_name, file_description=file_description, data=data)

        return [
            SystemMessage(system_message),
            HumanMessage(human_message)
        ]

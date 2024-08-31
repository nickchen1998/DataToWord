import abc
from typing import List
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures


class BaseLoader(abc.ABC):
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        self.llm = ChatOpenAI(
            openai_api_key=self.openai_api_key,
            model_name="gpt-4o-mini",
        )

    @abc.abstractmethod
    def create_documents(
            self,
            file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 1000,
    ) -> List[Document]:
        pass

    @abc.abstractmethod
    def parse_binary_content(self, file_binary_content: bytes):
        pass

    @abc.abstractmethod
    def generate_messages(self, file_name: str, file_description: str, data) -> List[BaseMessage]:
        pass

    def _generate_documents(self, file_name, file_description, datas, metadata: dict = None) -> List[Document]:

        documents = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(self.__invoke_llm, file_name, file_description, data, metadata)
                for data in datas
            ]
            for future in concurrent.futures.as_completed(futures):
                document = future.result()
                if "這是標頭" in document.page_content:
                    continue
                documents.append(future.result())

        return documents

    def __invoke_llm(self, file_name, file_description, data, metadata: dict = None) -> Document:
        messages = self.generate_messages(file_name, file_description, data)
        ai_message = self.llm.invoke(messages)
        document = Document(page_content=ai_message.content)
        if metadata:
            document.metadata = metadata

        return document

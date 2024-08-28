import abc
from typing import List
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI


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
            file_name: str, file_binary_content: bytes, file_description: str,
            chunk_size: int = 1000
    ) -> List[Document]:
        pass

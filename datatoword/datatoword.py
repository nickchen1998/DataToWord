import os

from datatoword.loaders.factory import LoaderFactory
from langchain_core.documents import Document
from typing import List


class DataToWord:
    def __init__(
            self,
            openai_api_key: str = None
    ):
        if openai_api_key is None:
            if os.getenv("OPENAI_API_KEY"):
                openai_api_key = os.getenv("OPENAI_API_KEY")
            else:
                raise ValueError("pass openai_api_key or set OPENAI_API_KEY in environment variable")
        self.openai_api_key = openai_api_key

    def create_documents(
            self,
            file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 1000
    ) -> List[Document]:
        loader = LoaderFactory().get_loader(file_name=file_name, openai_api_key=self.openai_api_key)

        documents = loader.create_documents(
            file_name=file_name,
            file_binary_content=file_binary_content,
            file_description=file_description,
            chunk_size=chunk_size,
            metadata=metadata
        )
        return documents

    def create_content(
            self,
            file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 1000
    ) -> List[str]:
        return [doc.page_content for doc in self.create_documents(
            file_name=file_name, file_binary_content=file_binary_content, file_description=file_description,
            metadata=metadata, chunk_size=chunk_size
        )]

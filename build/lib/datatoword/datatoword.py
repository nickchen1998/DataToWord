from datatoword.loaders.factory import LoaderFactory
from langchain_core.documents import Document
from typing import List


class DataToWord:
    def __init__(
            self,
            file_name: str, file_binary_content: bytes, file_description: str,
            openai_api_key: str
    ):
        self.loader = LoaderFactory().get_loader(file_name=file_name, openai_api_key=openai_api_key)
        self.file_description = file_description
        self.file_name = file_name
        self.file_binary_content = file_binary_content

    def create_documents(self, chunk_size: int = 1000) -> List[Document]:
        documents = self.loader.create_documents(
            file_name=self.file_name,
            file_binary_content=self.file_binary_content,
            file_description=self.file_description,
            chunk_size=chunk_size
        )
        return documents

    def create_content(self, chunk_size: int = 1000) -> List[str]:
        return [doc.page_content for doc in self.create_documents(chunk_size)]


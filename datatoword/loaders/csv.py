from . import BaseLoader
from langchain_community.document_loaders import CSVLoader as LangChainCSVLoader
from typing import List
from langchain_core.documents import Document


class CSVLoader(BaseLoader):
    def create_documents(
            self,
            file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 1000
    ) -> List[Document]:
        return []

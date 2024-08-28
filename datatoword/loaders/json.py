import json
from . import BaseLoader
from langchain_core.documents import Document
from typing import List
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage


class JSONLoader(BaseLoader):
    def create_documents(
            self, file_name: str, file_binary_content: bytes, file_description: str, metadata: dict = None,
            chunk_size: int = 300
    ) -> List[Document]:
        json_content = json.loads(file_binary_content.decode('utf-8'))
        splitter = RecursiveJsonSplitter(max_chunk_size=chunk_size)
        split_contents = splitter.split_json(json_data=json_content)

        return []

    def parse_binary_content(self, file_binary_content: bytes):
        pass

    def generate_messages(self, **kwargs) -> List[BaseMessage]:
        pass
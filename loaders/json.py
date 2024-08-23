import json
from . import BaseLoader
from langchain_core.documents import Document
from typing import List
from langchain_text_splitters import RecursiveJsonSplitter


class JSONLoader(BaseLoader):
    def create_documents(
            self, file_name: str, file_binary_content: bytes, file_description: str,
            chunk_size: int = 300
    ) -> List[Document]:
        json_content = json.loads(file_binary_content.decode('utf-8'))
        splitter = RecursiveJsonSplitter(max_chunk_size=chunk_size)
        split_contents = splitter.split_json(json_data=json_content)
        print(split_contents)
        print(self.openai_api_key)

        return []

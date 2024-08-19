import os
from . loader import JSONLoader
from langchain_community.document_loaders import CSVLoader


class LoaderFactory:
    loader_dict = {
        "json": JSONLoader,
        "csv": CSVLoader,
    }

    def __init__(self, file_path):
        self.file_path = file_path

    def get_loader(self):
        # 取得副檔名
        file_name = os.path.basename(self.file_path)
        ext = os.path.splitext(file_name)[-1].lower().replace('.', '')

        if not ext:
            raise ValueError(f"Cannot determine file extension from file name: {file_name}")

        # 根據副檔名選擇 loader
        if ext in self.loader_dict:
            return self.loader_dict[ext](self.file_path)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")
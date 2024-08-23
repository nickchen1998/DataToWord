import os
from . import BaseLoader
from .json import JSONLoader
from .csv import CSVLoader


class LoaderFactory:
    loader_dict = {
        "json": JSONLoader,
        "csv": CSVLoader,
    }

    def get_loader(self, file_name: str, openai_api_key: str) -> BaseLoader:
        if not file_name:
            raise ValueError("File name cannot be empty")

        ext = os.path.splitext(file_name)[1].lower().lstrip('.')

        if not ext:
            raise ValueError(f"Cannot determine file extension from file name: {file_name}")

        if ext in self.loader_dict:
            loader_class = self.loader_dict[ext]
            return loader_class(openai_api_key)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

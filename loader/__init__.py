import os
import abc
from typing import Union
from pathlib import Path
from langchain_community.document_loaders import CSVLoader


class BaseLoader(abc.ABC):
    def __init__(self, file_path: Union[str, Path]):
        self.file_path = file_path

    @abc.abstractmethod
    def load(self) -> str:
        pass



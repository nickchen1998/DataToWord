import os
import abc
from typing import Union
from pathlib import Path
from . import BaseLoader



class JSONLoader(BaseLoader):
    def load(self) -> str:
        import json
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data




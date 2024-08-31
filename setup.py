# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datatoword', 'datatoword.loaders']

package_data = \
{'': ['*']}

install_requires = \
['langchain-community>=0.2.12,<0.3.0',
 'langchain-openai>=0.1.22,<0.2.0',
 'langchain>=0.2.14,<0.3.0',
 'python-dotenv>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'datatoword',
    'version': '0.4.0',
    'description': '',
    'long_description': "# DataToWord\n\n## Built With\n\n- [Python](https://www.python.org/)\n- [Poetry](https://python-poetry.org/)\n- [LangChain](https://www.langchain.com/)\n- [OpenAI](https://platform.openai.com/docs/models)\n\n## 專案目的\n\n這是一個將資料轉換成文字的專案，可以協助你在進行 RAG 的過程中，將資料類型的檔案轉換成文字，提升轉換為向量後查詢的結果。\n\n目前支援的檔案有：\n\n- CSV\n- JSON\n\n\n## Quick Start\n\n- 建立 LangChain Document\n```python\nfrom datatoword import DataToWord\n\n\nwith open('data.csv', 'rb') as file:\n    file_binary_content = file.read()\n\ndata_to_word = DataToWord()\ndata_to_word.create_documents(\n    file_name='data.csv',\n    file_description='這是一個測試的檔案',\n    file_binary_content=file_binary_content\n)\n```\n\n- 取得轉換後的內文\n```python\nfrom datatoword import DataToWord\n\n\nwith open('data.csv', 'rb') as file:\n    file_binary_content = file.read()\n\ndata_to_word = DataToWord()\ndata_to_word.create_content(\n    file_name='data.csv',\n    file_description='這是一個測試的檔案',\n    file_binary_content=file_binary_content\n)\n```\n",
    'author': 'nick',
    'author_email': 'nickchen1998@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nickchen1998/DataToWord',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)


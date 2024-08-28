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
    'version': '0.2.0',
    'description': '',
    'long_description': '# DataToWord\n\n## 專案目的\n\n這是一個將資料轉換成文字的專案，可以協助你在進行 RAG 的過程中，將資料類型的檔案轉換成文字，方便後續進行段落查詢。\n\n目前支援的檔案有：\n\n- CSV\n- JSON\n\n## 使用方式\n\n### 安裝\n\n```bash\npip install datatoword\n```\nor\n\n```bash\npoetry add datatoword\n```\n\n### Quick Start\n\n```python\n```\n\n## poetry export requirements.txt\n\n```bash\npoetry export -f requirements.txt --output requirements.txt --without-hashes\n```',
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


# DataToWord

## Built With

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/docs/models)

## 專案目的

這是一個將資料轉換成文字的專案，可以協助你在進行 RAG 的過程中，將資料類型的檔案轉換成文字，提升轉換為向量後查詢的結果。

目前支援的檔案有：

- CSV
- JSON


## Quick Start

- 建立 LangChain Document
```python
from datatoword import DataToWord


with open('data.csv', 'rb') as file:
    file_binary_content = file.read()

data_to_word = DataToWord()
data_to_word.create_documents(
    file_name='data.csv',
    file_description='這是一個測試的檔案',
    file_binary_content=file_binary_content
)
```

- 取得轉換後的內文
```python
from datatoword import DataToWord


with open('data.csv', 'rb') as file:
    file_binary_content = file.read()

data_to_word = DataToWord()
data_to_word.create_content(
    file_name='data.csv',
    file_description='這是一個測試的檔案',
    file_binary_content=file_binary_content
)
```

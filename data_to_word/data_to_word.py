from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders.base import BaseLoader
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_core.prompts import ChatPromptTemplate
from loader.factory import LoaderFactory
from typing import Union
from pathlib import Path


class DataToWord:
    loader: BaseLoader
    chat_model: BaseChatModel

    def __init__(self, file_path: Union[str | Path], description: str, chat_model: BaseChatModel = None,
                 openai_api_key: str = None, ):
        if chat_model is None and openai_api_key is None:
            raise ValueError("Either chat_model or openai_api_key must be provided.")
        if chat_model is None and openai_api_key:
            self.chat_model = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key)
        if chat_model is not None:
            self.chat_model = chat_model

        self.loader = LoaderFactory(file_path).get_loader()
        self.description = description

    def parse(self, chunk_size: int = 1000):
        content = self.__get_content()


        chunk = 1000
        messages = [SystemMessage(content="""
            你是一個資料科學家，請根據我給你的檔案內容、檔案描述以及段落大小，描述一個到多個段落，每個段落請幫我用 ; 分隔。
            ----
            檔案描述：{description}
            段落大小：{chunk_size}
            ----
        """.format(description=self.description, chunk_size=chunk_size))]
        for i in range(0, len(content), chunk):
            chunk_content = content[i:i + chunk]
            messages.append(HumanMessage(content=f"這是第 {i // chunk} 個段落：{chunk_content}"))
            messages.append(AIMessage(content=f"好的，我收到你的第 {i // chunk} 個段落了。"))

        messages.append(HumanMessage(content="段落上傳完成，請幫我描述這個檔案。"))

        result = self.chat_model.invoke(input=messages)


        return result

    def __get_content(self):
        content = self.loader.load()

        return content


if __name__ == '__main__':
    # 資料源: https://data.gov.tw/dataset/166558
    BASE_DIR = Path(__file__).resolve().parent
    data_to_word = DataToWord(
        file_path=BASE_DIR / "test.json",
        openai_api_key="",
        description="""
        檔案名稱：
        檔案描述：提供農作物統一代碼與農業相關系統(包括農產品批發市場交易行情、農糧情調查、農產品產地價格、溯源農糧產品追溯及產銷供應鏈等系統)之農作物代碼對應；欄位包括農作物統一名稱、別名與代碼，以及對應之系統名稱與代號、農作物名稱與代碼。
        欄位描述：CROP_UID(農作物統一代碼)、CNAME(農作物中文名稱)、ALIAS_CNAME(農作物中文別名)、SRC_SYS_ID(來源系統代號)、SRC_NAME(來源系統名稱)、SRC_ID(來源系統農作物代碼)、SRC_CNAME(來源系統農作物中文名稱)
        """
    )
    print(data_to_word.parse())

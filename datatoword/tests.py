import os

import pytest
from dotenv import load_dotenv
from pathlib import Path


class TestDataToWord:

    @pytest.fixture(autouse=True)
    def openai_api_key(self):
        if os.getenv("OPENAI_API_KEY"):
            openai_api_key = os.getenv("OPENAI_API_KEY")
        else:
            load_dotenv(Path(__file__).resolve().parent.parent / ".env")
            openai_api_key = os.getenv("OPENAI_API_KEY")

        if openai_api_key is None:
            raise ValueError("pass openai_api_key or set OPENAI_API_KEY in environment variable")

        return openai_api_key

    def test_data_to_word(self, openai_api_key):
        file_name = 'test_file.csv'
        file_binary = b'''
            name,age,position,skills,project_name,project_duration_months,project_team_size
            Alice Smith,30,Software Engineer,"Python;Django;Machine Learning","AI Chatbot",12,5
            Alice Smith,30,Software Engineer,"Python;Django;Machine Learning","E-commerce Platform",8,3
            Bob Johnson,35,Data Scientist,"Python;Pandas;Deep Learning","Data Analysis Pipeline",6,4
            Bob Johnson,35,Data Scientist,"Python;Pandas;Deep Learning","Recommendation System",10,7
        '''
        file_description = "這是一份描寫員供資料的 csv 檔。"

        from datatoword import DataToWord

        data_to_word = DataToWord(openai_api_key=openai_api_key)
        documents = data_to_word.create_documents(
            file_name=file_name,
            file_binary_content=file_binary,
            file_description=file_description,
        )
        print(documents)

        assert documents is not None

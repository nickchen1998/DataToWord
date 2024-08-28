class TestDataToWord:

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

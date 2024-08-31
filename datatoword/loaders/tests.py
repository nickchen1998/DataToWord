class TestLoader:

    def test_json_loader(self, openai_api_key):
        file_name = "Tech Innovators Inc data.json"
        file_binary_content = b'''
        {
            "company": {
                "name": "Tech Innovators Inc.",
                "founded": 2010,
                "employees": [
                    {
                        "name": "Alice Smith",
                        "age": 30,
                        "position": "Software Engineer",
                        "skills": ["Python", "Django", "Machine Learning"],
                        "projects": [
                            {"name": "AI Chatbot", "duration_months": 12, "team_size": 5},
                            {"name": "E-commerce Platform", "duration_months": 8, "team_size": 3}
                        ]
                    },
                    {
                        "name": "Bob Johnson",
                        "age": 35,
                        "position": "Data Scientist",
                        "skills": ["Python", "Pandas", "Deep Learning"],
                        "projects": [
                            {"name": "Data Analysis Pipeline", "duration_months": 6, "team_size": 4},
                            {"name": "Recommendation System", "duration_months": 10, "team_size": 7}
                        ]
                    }
                ],
                "departments": [
                    {
                        "name": "Engineering",
                        "budget_million_usd": 10,
                        "head": "John Doe"
                    },
                    {
                        "name": "Research and Development",
                        "budget_million_usd": 15,
                        "head": "Jane Roe"
                    }
                ]
            }
        }
        '''
        file_description = "Tech Innovators Inc. 的基本資訊。"

        from datatoword.loaders.json import JSONLoader

        json_loader = JSONLoader(openai_api_key=openai_api_key)

        documents = json_loader.create_documents(
            file_name=file_name,
            file_binary_content=file_binary_content,
            file_description=file_description,
            chunk_size=300
        )
        for document in documents:
            print(document)

        assert documents is not None

    def test_csv_loader(self, openai_api_key):
        file_name = 'test_file.csv'
        file_binary = b'''
            name,age,position,skills,project_name,project_duration_months,project_team_size
            Alice Smith,30,Software Engineer,"Python;Django;Machine Learning","AI Chatbot",12,5
            Alice Smith,30,Software Engineer,"Python;Django;Machine Learning","E-commerce Platform",8,3
            Bob Johnson,35,Data Scientist,"Python;Pandas;Deep Learning","Data Analysis Pipeline",6,4
            Bob Johnson,35,Data Scientist,"Python;Pandas;Deep Learning","Recommendation System",10,7
        '''
        file_description = "這是一份描寫員供資料的 csv 檔。"

        from datatoword.loaders.csv import CSVLoader

        documents = CSVLoader(openai_api_key=openai_api_key).create_documents(
            file_name=file_name,
            file_binary_content=file_binary,
            file_description=file_description,
            chunk_size=300
        )
        for document in documents:
            print(document.page_content)

        assert documents is not None

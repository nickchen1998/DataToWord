import os

import pytest
from langchain_core.documents import Document
from typing import List
from dotenv import load_dotenv
from pathlib import Path


class TestLoader:

    @pytest.fixture(autouse=True)
    def openai_api_key(self):
        if os.getenv("OPENAI_API_KEY"):
            openai_api_key = os.getenv("OPENAI_API_KEY")
        else:
            load_dotenv(Path(__file__).resolve().parent.parent / ".env")
            openai_api_key = os.getenv("OPENAI_API_KEY")

        return openai_api_key


    def test_json_loader(self, openai_api_key):
        file_name = "test_file.json"
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
            },
            "location": {
                "headquarters": {
                    "city": "San Francisco",
                    "state": "CA",
                    "country": "USA"
                },
                "offices": [
                    {"city": "New York", "state": "NY", "country": "USA"},
                    {"city": "London", "state": "N/A", "country": "UK"},
                    {"city": "Berlin", "state": "N/A", "country": "Germany"}
                ]
            },
            "products": [
                {
                    "name": "Smart AI Assistant",
                    "category": "Software",
                    "price_usd": 49.99,
                    "features": ["Voice Recognition", "Natural Language Processing", "Cloud Sync"]
                },
                {
                    "name": "Advanced Analytics Platform",
                    "category": "Software",
                    "price_usd": 299.99,
                    "features": ["Real-time Data Processing", "Customizable Dashboards", "AI-powered Insights"]
                }
            ]
        }
        '''
        file_description = "Tech Innovators Inc. 的基本資訊。"

        from loaders.json import JSONLoader

        json_loader = JSONLoader(openai_api_key=openai_api_key)

        documents = json_loader.create_documents(
            file_name=file_name,
            file_binary_content=file_binary_content,
            file_description=file_description,
            chunk_size=300
        )

        assert json_loader.openai_api_key is not None

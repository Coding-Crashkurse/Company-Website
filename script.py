import requests

API_URL = "http://localhost:5555/api/courses"

courses_data = [
    {
        "title": "LangGraph in Action: Develop Advanced AI Agents with LLMs",
        "price": 54.99,
        "link": "https://www.udemy.com/course/langgraph-in-action-develop-advanced-ai-agents-with-llms/",
        "image": "https://img-c.udemycdn.com/course/750x422/6359927_fb55.jpg",
    },
    {
        "title": "Advanced LangChain Techniques: Mastering RAG Applications",
        "price": 49.99,
        "link": "https://www.udemy.com/course/advanced-langchain-techniques-mastering-rag-applications/",
        "image": "https://img-c.udemycdn.com/course/750x422/6052857_31ba_2.jpg",
    },
    {
        "title": "LangChain on Azure - Building Scalable LLM Applications",
        "price": 34.99,
        "link": "https://www.udemy.com/course/langchain-on-azure-building-scalable-llm-applications/",
        "image": "https://img-c.udemycdn.com/course/750x422/5734832_ba74.jpg",
    },
    {
        "title": "LangChain in Action: Develop LLM-Powered Apps",
        "price": 54.99,
        "link": "https://www.udemy.com/course/langchain-in-action-develop-llm-powered-apps/",
        "image": "https://img-c.udemycdn.com/course/750x422/5621170_d56e.jpg",
    },
    {
        "title": "FastAPI für Anfänger - Baue einen Twitter Clone mit FastAPI",
        "price": 44.99,
        "link": "https://www.udemy.com/course/fastapi-fuer-anfaenger-baue-einen-twitter-clone-mit-fastapi/",
        "image": "https://img-c.udemycdn.com/course/750x422/5055186_4547_3.jpg",
    },
]


def create_courses():
    for course in courses_data:
        response = requests.post(API_URL, json=course)
        if response.status_code in (200, 201):
            print("Created course:", response.json())
        else:
            print(f"Failed to create course '{course['title']}':", response.text)


if __name__ == "__main__":
    create_courses()

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    USER_MAP = {
        "john": {"jira": "john@example.com", "github": "john-gh"},
        "mike": {"jira": "mike@example.com", "github": "mike-gh"},
        "lisa": {"jira": "lisa@example.com", "github": "lisa-gh"},
        "sarah": {"jira": "sarah@example.com", "github": "sarah-gh"},
    }
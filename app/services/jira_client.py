import requests
from app.core.config import Config


def get_user_issues(user_email: str):
    """
    Fetch assigned JIRA issues for a user.
    """
    url = f"{Config.JIRA_BASE_URL}/rest/api/3/search"

    params = {
        "jql": f"assignee={user_email} AND updated >= -7d ORDER BY updated DESC",
        "maxResults": 5
    }

    response = requests.get(
        url,
        params=params,
        auth=(Config.JIRA_EMAIL, Config.JIRA_API_TOKEN)
    )

    data = response.json()

    return [
        {
            "key": issue["key"],
            "summary": issue["fields"]["summary"],
            "status": issue["fields"]["status"]["name"]
        }
        for issue in data.get("issues", [])
    ]
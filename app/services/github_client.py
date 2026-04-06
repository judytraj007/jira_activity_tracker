import requests
from app.core.config import Config

HEADERS = {
    "Authorization": f"token {Config.GITHUB_TOKEN}"
}


def get_commits(username: str):
    """
    Fetch recent commits by user.
    """
    url = "https://api.github.com/search/commits"

    params = {
        "q": f"author:{username}",
        "sort": "author-date",
        "order": "desc",
        "per_page": 5
    }

    headers = HEADERS.copy()
    headers["Accept"] = "application/vnd.github.cloak-preview"

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    return [
        {
            "message": item["commit"]["message"],
            "repo": item["repository"]["full_name"]
        }
        for item in data.get("items", [])
    ]


def get_prs(username: str):
    """
    Fetch recent pull requests.
    """
    url = "https://api.github.com/search/issues"

    params = {
        "q": f"author:{username} type:pr",
        "sort": "updated",
        "order": "desc",
        "per_page": 5
    }

    res = requests.get(url, headers=HEADERS, params=params)

    return res.json().get("items", [])
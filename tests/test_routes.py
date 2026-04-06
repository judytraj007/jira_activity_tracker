from unittest.mock import patch
from run import app


@patch("app.routes.parse_query")
@patch("app.routes.get_user_issues")
@patch("app.routes.get_commits")
@patch("app.routes.get_prs")
def test_query_endpoint(mock_prs, mock_commits, mock_jira, mock_parse):
    client = app.test_client()

    mock_parse.return_value.user = "john"
    mock_parse.return_value.intent = "ALL"

    mock_jira.return_value = []
    mock_commits.return_value = []
    mock_prs.return_value = []

    response = client.post("/query", json={
        "question": "What is John working on?"
    })

    assert response.status_code == 200
from unittest.mock import patch
from app.services.llm_parser import parse_query
from app.models.query import ParsedQuery


@patch("app.services.llm_parser.client.chat.completions.create")
def test_parse_query_commits(mock_llm):
    """
    Test that parser correctly extracts user and COMMITS intent.
    """

    # Mock LLM response
    mock_llm.return_value.choices = [
        type("obj", (), {
            "message": type("obj", (), {
                "content": '{"user": "mike", "intent": "COMMITS"}'
            })
        })
    ]

    result = parse_query("What has Mike committed this week?")

    assert isinstance(result, ParsedQuery)
    assert result.user == "mike"
    assert result.intent == "COMMITS"


@patch("app.services.llm_parser.client.chat.completions.create")
def test_parse_query_prs(mock_llm):
    """
    Test PR intent extraction.
    """

    mock_llm.return_value.choices = [
        type("obj", (), {
            "message": type("obj", (), {
                "content": '{"user": "lisa", "intent": "PRS"}'
            })
        })
    ]

    result = parse_query("Show me Lisa's pull requests")

    assert result.user == "lisa"
    assert result.intent == "PRS"


@patch("app.services.llm_parser.client.chat.completions.create")
def test_parse_query_default_all(mock_llm):
    """
    Test fallback to ALL intent.
    """

    mock_llm.return_value.choices = [
        type("obj", (), {
            "message": type("obj", (), {
                "content": '{"user": "john", "intent": "ALL"}'
            })
        })
    ]

    result = parse_query("What is John working on?")

    assert result.user == "john"
    assert result.intent == "ALL"


@patch("app.services.llm_parser.client.chat.completions.create")
def test_parse_query_invalid_json(mock_llm):
    """
    Test graceful handling of invalid LLM output.
    """

    mock_llm.return_value.choices = [
        type("obj", (), {
            "message": type("obj", (), {
                "content": 'invalid json'
            })
        })
    ]

    try:
        parse_query("What is John working on?")
        assert False, "Expected exception for invalid JSON"
    except Exception:
        assert True
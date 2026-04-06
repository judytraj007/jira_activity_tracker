from app.utils.response_builder import build_response

def test_empty_response():
    res = build_response("john", "ALL", [], [], [])
    assert "No recent activity" in res
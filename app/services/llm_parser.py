import json
from openai import OpenAI
from app.core.config import Config
from app.models.query import ParsedQuery

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def parse_query(query: str) -> ParsedQuery:
    """
    Uses LLM to extract user and intent from natural language query.
    """

    prompt = f"""
    Extract the following from the query:
    1. user name
    2. intent (one of: COMMITS, PRS, JIRA, ALL)

    Query: "{query}"

    Respond ONLY in JSON:
    {{
        "user": "...",
        "intent": "..."
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    return ParsedQuery(
        user=data["user"].lower(),
        intent=data["intent"]
    )
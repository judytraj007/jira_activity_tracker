from flask import Blueprint, request, jsonify
from concurrent.futures import ThreadPoolExecutor

from app.services.llm_parser import parse_query
from app.services.jira_client import get_user_issues
from app.services.github_client import get_commits, get_prs
from app.utils.response_builder import build_response
from app.core.config import Config

bp = Blueprint("routes", __name__)


@bp.route("/query", methods=["POST"])
def query():
    data = request.json
    question = data.get("question")

    parsed = parse_query(question)

    if parsed.user not in Config.USER_MAP:
        return jsonify({"error": "User not found"}), 404

    user_map = Config.USER_MAP[parsed.user]

    jira = commits = prs = []

    with ThreadPoolExecutor() as executor:
        futures = []

        if parsed.intent in ["ALL", "JIRA"]:
            futures.append(("jira", executor.submit(get_user_issues, user_map["jira"])))

        if parsed.intent in ["ALL", "COMMITS"]:
            futures.append(("commits", executor.submit(get_commits, user_map["github"])))

        if parsed.intent in ["ALL", "PRS"]:
            futures.append(("prs", executor.submit(get_prs, user_map["github"])))

        for key, future in futures:
            if key == "jira":
                jira = future.result()
            elif key == "commits":
                commits = future.result()
            elif key == "prs":
                prs = future.result()

    response = build_response(parsed.user, parsed.intent, jira, commits, prs)

    return jsonify({"response": response})
def build_response(user, intent, jira, commits, prs):
    """
    Build human-readable response.
    """

    if not any([jira, commits, prs]):
        return f"No recent activity found for {user}."

    response = f"{user.capitalize()}'s activity:\n\n"

    if intent in ["ALL", "JIRA"] and jira:
        response += "JIRA:\n"
        for j in jira:
            response += f"- {j['key']}: {j['summary']} ({j['status']})\n"

    if intent in ["ALL", "COMMITS"] and commits:
        response += "\nCommits:\n"
        for c in commits:
            response += f"- {c['message']} ({c['repo']})\n"

    if intent in ["ALL", "PRS"] and prs:
        response += "\nPRs:\n"
        for pr in prs:
            response += f"- {pr['title']}\n"

    return response
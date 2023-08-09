import os

import marvin
from marvin import ai_fn
from prefect import flow


@ai_fn
def summarize_github_issue(issue_text: str) -> str:
    """
    Given the github issue text, summarize it
    """

@flow
def summarize_issue(issue_number: int, issue_text: str, user_login_name: str) -> str:
    key = os.environ["OPENAI_API_KEY"]
    marvin.settings.openai.api_key = key
    return summarize_github_issue(issue_text)

if __name__ == "__main__":
    summarize_issue(123455, "I'm upset because I called my flow function and it returned an error that said 'No flow function found'", "jlowin")

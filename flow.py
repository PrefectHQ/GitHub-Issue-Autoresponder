import os

import marvin
import requests
from marvin import ai_fn
from prefect import flow, task, get_run_logger


@ai_fn
def summarize_github_issue(issue_text: str) -> str:
    """
    Given the github issue text, summarize it
    """

@ai_fn
@task
def marvin_response(issue_text: str) -> str:
    """
    Given the github issue text, provide a friendly suggestion for a work around in Prefect 2.0. 
    If a work around does not exist, return a message saying that the team at Prefect is looking into it. 
    """


@task
def issue_comment(owner: str, repo: str, issue_number: str, message: str):
    """Issue comment event."""
    github_api_key = os.environ["GITHUB_API_KEY"]
    token = f"Authorization: Bearer {github_api_key}"
    requests.post(f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments",data=message, headers=token)

@flow
def suggested_fix_from_marvin(issue_number: int, issue_text: str, user_login_name: str) -> None:
    open_api_key = os.environ["OPENAI_API_KEY"]
    marvin.settings.openai.api_key = open_api_key
    
    summary = summarize_github_issue(issue_text)
    response = marvin_response(summary)
    logger = get_run_logger()
    logger.info(response)
    if response:
        issue_comment("PrefectHQ", "Project-2-TPV-GTM-Relay", issue_number, response)
    
    return None

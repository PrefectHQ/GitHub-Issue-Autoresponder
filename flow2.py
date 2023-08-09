
from marvin import ai_fn
from prefect import flow, task

@ai_fn
@task
def marvin_response(issue_text: str) -> str:
    """
    Given the github issue text, provide a friendly suggestion for a work around in Prefect 2.0. 
    If a work around does not exist, return a message saying that the team at Prefect is looking into it. 
    """



@flow()
def main(text : str):
    return marvin_response(issue_text = text)

if __name__ == "__main__":
    r = main("My Prefect 2.0 flow is in a crashed state. What should I do?")
    print(r)

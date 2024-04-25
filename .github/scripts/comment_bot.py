"""
Script for Comment Bot. 

Comments on new PR or Issues, 
informing on how to trigger the 
Self-Assign bot.
"""
import os
from github import Github

def main():
    # Initialize a Github instance:
    g = Github(os.getenv("GITHUB_TOKEN"))
    
    # Get the repo from environment variables
    repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))

    # Get the event type (issue or pull request)
    event_type = os.getenv("EVENT_TYPE")

    # Get the issue or pull request number from the event payload
    issue_number = int(os.getenv("ISSUE_NUMBER"))

    # Get the issue or pull request object
    if event_type == "issues":
        issue = repo.get_issue(number=issue_number)
    elif event_type == "pull_request":
        issue = repo.get_pull(number=issue_number)

    # Comment on the issue or pull request with instructions to trigger the Self-Assign bot
    comment_body = f"""
    To assign yourself to this {event_type}, please mention '@your_username' and use one of the following trigger phrases:
    - Aeon-Assign bot
    - assign this to
    - please assign

    For example: 'Aeon-Assign bot assign @your-username'
    """
    issue.create_comment(comment_body.strip())

if __name__ == "__main__":
    main()

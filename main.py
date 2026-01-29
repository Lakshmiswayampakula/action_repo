"""
Action Repo - Main Python File

This file is used to trigger GitHub webhook events.
Make changes to this file and push to trigger PUSH events.
Create pull requests to trigger PULL_REQUEST events.
Merge pull requests to trigger MERGE events.
"""

def main():
    """Main function for action-repo."""
    print("Action Repo - GitHub Webhook Trigger")
    print("This repository triggers webhook events to the webhook receiver.")
    print("Make commits, create PRs, and merge to test webhook functionality.")


if __name__ == "__main__":
    main()

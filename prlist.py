from github import Github
import datetime
import os

owner, repository = os.getenv('GH_REPO').split("/")
gh = Github(os.getenv('GH_TOKEN'))
merge_pr_title(os.getenv('MERGE_PR_TITLE'))

open_prs = []
rep = gh.get_user(owner).get_repo(repository)
pulls = rep.get_pulls(state="open")

for pull in pulls:
    if pull.title.startswith("DEPLOYMENT-CODE-FREEZE"):
        print(f"::error title=Deployment code freeze")
        exit 1
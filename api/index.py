import os
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# DEFINE ENVIRONMENT VARIABLES
GITHUB_KEY = os.environ.get('GITHUB_KEY')
NOTION_KEY = os.environ.get('NOTION_KEY')

@app.get("/api/syncHelpingHandsIssues")
def syncHelpingHandsIssues():
    url = "https://api.github.com/repos/Jorge-lopz/Helping-Hands/issues"
    headers = {
        "Accept": "application/vnd.github.text+json",
        "Authorization": f"Bearer {GITHUB_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        return None
from pathlib import Path
import json
from fasthtml.oauth import GitHubAppClient, GoogleAppClient
from hugging_face_auth import HuggingFaceClient

current_dir = Path(__file__).parent
secrets_path = current_dir / "secrets"

host,port = 'localhost',8000
redirect_url = f"http://{host}:{port}/callback"

# Github Login
with open('secrets/github.json') as f:
    secrets_github = json.load(f)

github_client_id = secrets_github['github']['client_id']
github_client_secret = secrets_github['github']['client_secret']

github_client = GitHubAppClient(
    client_id=github_client_id,
    client_secret=github_client_secret,
    redirect_uri=redirect_url,
)

# Google Login
with open('secrets/google.json') as f:
    secrets_google = json.load(f)

google_client_id = secrets_google['web']['client_id']
google_client_secret = secrets_google['web']['client_secret']
google_client = GoogleAppClient(
    client_id= google_client_id,
    client_secret= google_client_secret,
    redirect_uri=redirect_url
)

# HuggingFace Login
with open('secrets/huggingface.json') as f:
    secrets_huggingface = json.load(f)

huggingface_client_id = secrets_huggingface['huggingface']['client_id']
huggingface_client_secret = secrets_huggingface['huggingface']['client_secret']

huggingface_client = HuggingFaceClient(
    client_id=huggingface_client_id,
    client_secret=huggingface_client_secret,
    redirect_uri=redirect_url
)


def github_login_link():
    return github_client.login_link()

def google_login_link():
    return google_client.login_link()

def huggingface_login_link():
    return huggingface_client.login_link()










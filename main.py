from fasthtml.common import FastHTML, Button
import uvicorn
import os
from oauth import github_login_link, google_login_link, huggingface_login_link, github_client, google_client, huggingface_client

app = FastHTML()
rt = app.route

@rt("/")
def get():
    github_url = github_login_link()
    google_url = google_login_link()
    huggingface_url = huggingface_login_link()

    return (
        Button("Login with Github", onclick=f"window.location.href = '{github_url}';"),
        Button("Login with Google", onclick=f"window.location.href = '{google_url}';"),
        Button("Login with HuggingFace", onclick=f"window.location.href = '{huggingface_url}';")
    )


@rt("/callback", methods=["GET"])
def callback(request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")

    if 'state' in request.query_params:
        client = huggingface_client
        provider = 'huggingface'
    elif 'scope' in request.query_params:
        client = google_client
        provider = 'google'
    else:
        client = github_client
        provider = 'github'

    try:
        user_info = client.retr_info(code)
    except Exception as e:
        error_message = str(e)
        print(f"Error occurred: {error_message}")
        return f"An error occurred: {error_message}"

    if provider == 'github':
        user_name = user_info.get("login")
    elif provider == 'google':
        user_name = user_info.get("name")
    elif provider == 'huggingface':
        user_name = user_info.get("preferred_username")

    return f"Hello, {user_name}!"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))

import requests

class HuggingFaceClient:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.auth_url = "https://huggingface.co/oauth/authorize"
        self.token_url = "https://huggingface.co/oauth/token"
        self.userinfo_url = "https://huggingface.co/oauth/userinfo"

    def login_link(self):
        return f"{self.auth_url}?client_id={self.client_id}&redirect_uri={self.redirect_uri}&response_type=code"

    def get_access_token(self, code):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(self.token_url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def retr_info(self, code):
        token_response = self.get_access_token(code)
        access_token = token_response['access_token']
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(self.userinfo_url, headers=headers)
        response.raise_for_status()
        return response.json()

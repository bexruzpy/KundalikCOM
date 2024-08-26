import requests
import json
class ServerConnect(object):
    """docstring for ServerConnect"""
    def __init__(self):
        super(ServerConnect, self).__init__()
        self.asosiy_url = "http://127.0.0.1:8000"
        # self.asosiy_url = "https://api.projectsplatform.uz"
    def post_request(self, url: str, data):
        result = requests.post(self.asosiy_url+url,
            headers={
                'accept': 'application/json',
                'Content-Type': 'application/json'
            },
            data=json.dumps(data))
        return result.json()
    # Telegramdan kod olish uchun
    def get_login(self, username, password):
        return self.post_request("/accounts/login", {
          "username": "alone",
          "password": "abdeix"
        })
    # login qilish
    def login(self, username, password, kod):
        return self.post_request("/accounts/check-login-code", {
          "username": username,
          "password": password,
          "code": kod
        })
    def about_user(self, token):
        pass
# server = ServerConnect()
# username = input("username: ").strip()
# password = input("password: ").strip()
# server.get_login("alone", "abdeix")
# print(server.login("alone", "abdeix", int(input("     kod: "))))

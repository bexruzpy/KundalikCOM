import requests
import json

import unical_id

class ServerConnect(object):
    """docstring for ServerConnect"""
    def __init__(self):
        super(ServerConnect, self).__init__()
        # self.asosiy_url = "http://127.0.0.1:8000"
        self.asosiy_url = "https://api.projectsplatform.uz"
    def post_request(self, url: str, data):
        # print(data)
        result = requests.post(self.asosiy_url+url,
            headers={
                'accept': 'application/json',
                'Content-Type': 'application/json'
            },
            data=json.dumps(data))
        # print(result.text)
        return result.json()
    # Telegramdan kod olish uchun
    def get_login(self, username, password):
        return self.post_request("/accounts/login", {
          "username": username,
          "password": password
        })
    # login qilish
    def login(self, username, password, kod):
        return self.post_request("/accounts/check-login-code", {
          "username": username,
          "password": password,
          "code": kod
        })
    def about_user(self, token):
        return self.post_request("/accounts/about_account", {"token": token})
    def check(self, token):
        devise_id = unical_id.get()
        return self.post_request("/kundalikcom/check_pc", {"token": token, "device_id": devise_id})
    def set_school(self, token: str, viloyat: str, tuman: str, maktab_nomi: str) -> dict:
        try:
            self.post_request("/kundalikcom/set_school", {
            "token": token,
            "tuman": tuman,
            "viloyat": viloyat,
            "school_name": maktab_nomi
            })
        except Exception as e:
            # print(e)
            pass
    def get_school(self, token: str) -> dict:
        return self.post_request("/kundalikcom/get_school", {
            "token": token
        })
    def get_pc_price(self):
        price_1 = self.post_request("/kundalikcom/price_months", {"months_count": 1})
        price_2 = self.post_request("/kundalikcom/price_months", {"months_count": 10})//10
        return price_1, price_2
    def get_pc_months_price(self, months_count: int):
        return self.post_request("/kundalikcom/price_months", {"months_count": months_count})
    def buy(self, token: str, months_count: int):
        return self.post_request("/kundalikcom/buy", {
            "token": token,
            "months_count": months_count
        })
# server = ServerConnect()
# username = input("username: ").strip()
# password = input("password: ").strip()
# server.get_login("alone", "abdeix")
# print(server.login("alone", "abdeix", int(input("     kod: "))))

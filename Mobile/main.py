from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from database import DatabaseConnection
import requests
import json

Builder.load_file("Login.kv")
Builder.load_file("Home.kv")
Builder.load_file("Datas.kv")
Builder.load_file("Let.kv")



# O'chiriladi
######################################
from kivy.core.window import Window
Window.size = (400, 600)
######################################

class LoginScreen(Screen):
    def get_login_code(self, username, password):
        res = requests.post("https://api.projectsplatform.uz/accounts/login", json={"username": username, "password": password})
        print(res.json())
    def login_func(self, username, password, code):
        try:
            res = requests.post("https://api.projectsplatform.uz/accounts/check-login-code", json={"username": username, "password": password, "code": int(code)})
            app.database.set_data("token", res.json()["token"])
            app.root.current = "home"
        except:
            pass
    def logout(self):
        app.database.logout()
        app.root.current = "login"

class HomeScreen(Screen):
    pass
class DatasScreen(Screen):
    pass
class LetsenziyaScreen(Screen):
    pass


class RootWidget(ScreenManager):
    # Ekranlarni `ScreenManager` ichida yaratish
    def __init__(self, page_name, **kwargs):
        super().__init__(**kwargs)
        self.LoginPage = LoginScreen(name="login")
        self.add_widget(self.LoginPage)
        self.HomePage = HomeScreen(name="home")
        self.add_widget(self.HomePage)
        self.LetsenziyaPage = LetsenziyaScreen(name="letsenziya")
        self.add_widget(self.LetsenziyaPage)
        self.DatasPage = DatasScreen(name="datas")
        self.add_widget(self.DatasPage)
        self.transition.direction = 'up'
        self.current = page_name

class KundalikCOMApp(App):
    def build(self):
        self.database = DatabaseConnection()
        print(self.database.device_id)
        token = self.database.get_data("token")
        if token:
            self.root = RootWidget(page_name="home")
        else:
            self.root = RootWidget(page_name="login")
        return self.root


    def login(self, username, password, sms_code):
        # Bu yerda to'liq loginni tasdiqlash funksiyasini qo'shishingiz mumkin
        print(f"Login Button pressed! Username: {username}, Password: {password}, SMS code: {sms_code}")

if __name__ == '__main__':
    app = KundalikCOMApp()
    app.run()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from kivy.lang import Builder
from database import DatabaseConnection
import requests
from datetime import datetime
from threading import Thread
from kivy.clock import Clock

Builder.load_file("Login.kv")
Builder.load_file("Home.kv")
Builder.load_file("Datas.kv")
Builder.load_file("Let.kv")



# O'chiriladi
######################################
from kivy.core.window import Window
Window.size = (400, 600)
######################################

class MessagePopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = ""
        self.separator_height = 0
    def set(self, title, text):
        self.ids.title.text = title
        self.ids.text.text = text
        self.open()

class ErrorPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "0"
        self.separator_height = 0
    def set(self, title, text):
        self.ids.title.text = title
        self.ids.text.text = text
        self.open()





class LoginScreen(Screen):
    def get_login_code(self, username, password):
        res = requests.post("https://api.projectsplatform.uz/accounts/login", json={"username": username, "password": password})
        print(res.json())
    def login_func(self, username, password, code):
        try:
            res = requests.post("https://api.projectsplatform.uz/accounts/check-login-code", json={"username": username, "password": password, "code": int(code)})
            app.database.set_data("token", res.json()["token"])
            app.root.current = "home"
            app.database.set_datas(self.get_full_data(res.json()["token"]))
            app.data_population()
        except:
            pass
    def get_full_data(self, token):
        res = requests.post("https://api.projectsplatform.uz/accounts/about_account", json={"token": token})
        return res.json()
    def logout(self):
        app.database.logout()
        app.root.current = "login"

class HomeScreen(Screen):
    def __init__(self, **r):
        super().__init__(**r)
        self.show_message = app.show_message
    def set_datas(self, text, rang):
        self.ids.letsenziya_label.text = text
        self.ids.letsenziya_label.color = rang
        fullname = app.database.get_data("full_name")
        if fullname != None:
            if len(fullname) >= 13:
                fullname = fullname[:10]+"..."
            self.ids.fullname.text = fullname
        else:
            app.root.manager.current = "login"
        self.ids.letsenziya_label.color = rang
class DatasScreen(Screen):
    def set_container(self, content_name):
        if content_name == "all":
            self.ids.datas_all_button.canvas.before.clear()
            with self.ids.datas_all_button.canvas.before:
                Color(0.4667, 0.2392, 0.7922, 1.0)
                RoundedRectangle(pos=(self.ids.datas_all_button.pos[0] + 5, self.ids.datas_all_button.pos[1] + 5), size=(self.ids.datas_all_button.size[0]-10,self.ids.datas_all_button.size[1]-10), radius=[18])

            self.ids.datas_err_button.canvas.before.clear()
            with self.ids.datas_err_button.canvas.before:
                Color(0.1490, 0.0000, 1.0000, 0.21)
                RoundedRectangle(pos=(self.ids.datas_err_button.pos[0] + 5, self.ids.datas_err_button.pos[1] + 5), size=(self.ids.datas_err_button.size[0]-10,self.ids.datas_err_button.size[1]-10), radius=[18])
        else:
            self.ids.datas_all_button.canvas.before.clear()
            with self.ids.datas_all_button.canvas.before:
                Color(0.1490, 0.0000, 1.0000, 0.21)
                RoundedRectangle(pos=(self.ids.datas_all_button.pos[0] + 5, self.ids.datas_all_button.pos[1] + 5), size=(self.ids.datas_all_button.size[0]-10,self.ids.datas_all_button.size[1]-10), radius=[18])

            self.ids.datas_err_button.canvas.before.clear()
            with self.ids.datas_err_button.canvas.before:
                Color(0.4667, 0.2392, 0.7922, 1.0)
                RoundedRectangle(pos=(self.ids.datas_err_button.pos[0] + 5, self.ids.datas_err_button.pos[1] + 5), size=(self.ids.datas_err_button.size[0]-10,self.ids.datas_err_button.size[1]-10), radius=[18])

    def set_datas(self, text, rang):
        self.ids.letsenziya_label.text = text
        self.ids.letsenziya_label.color = rang
        fullname = app.database.get_data("full_name")
        if fullname != None:
            if len(fullname) >= 13:
                fullname = fullname[:10]+"..."
            self.ids.fullname.text = fullname
        else:
            app.root.manager.current = "login"
    
    def get_datas(self):
        pass
class LetsenziyaScreen(Screen):
    def set_datas(self, text, rang):
        self.ids.letsenziya_label.text = text
        self.ids.letsenziya_label.color = rang
        fullname = app.database.get_data("full_name")
        if fullname != None:
            if len(fullname) >= 13:
                fullname = fullname[:10]+"..."
            self.ids.fullname.text = fullname
        else:
            app.root.manager.current = "login"


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
        token = self.database.get_data("token")
        if token:
            self.root = RootWidget(page_name="home")
            
            Clock.schedule_once(lambda dt: self.data_population())
        else:
            self.root = RootWidget(page_name="login")
        return self.root
    def data_population(self):
        try:
            res = requests.post("https://api.projectsplatform.uz/kundalikcom/check_mobile", json={"token": self.database.get_data("token"), "device_id": self.database.get_data("device_id")})
            self.letsenziya_data(res.json())
        except:
            self.show_error("Xatolik!", "Hisobingizga qayta kiring")
            self.root = RootWidget(page_name="login")
    def letsenziya_data(self, data):
        if 'end_active_date' in data:
            end_date = datetime.fromisoformat(data['end_active_date'])
            
            # Vaqtni formatlash
            formatted_date = end_date.strftime('%d.%m.%Y')
            if data['size'] > 0:
                rang = (0, 0.231, 0.435, 1)
                text = f"{formatted_date}y"
            else:
                rang = (1, 0, 0, 1)
                text = """letstenziyangiz tugagan"""
                self.show_error("Letsenziya", "Kechirasiz sizning letsenziyangiz tugagan!\nDasturdan foydalanish uchun xarid amalga oshirishingiz kerak!")

            Clock.schedule_once(lambda dt: self.root.get_screen('home').set_datas(text, rang))
            Clock.schedule_once(lambda dt: self.root.get_screen('datas').set_datas(text, rang))
            Clock.schedule_once(lambda dt: self.root.get_screen('letsenziya').set_datas(text, rang))
    def show_message(self, title, text):
        popup = MessagePopup()
        popup.set(title, text)
    def show_error(self, title, text):
        popup = ErrorPopup()
        popup.set(title, text)


if __name__ == '__main__':
    app = KundalikCOMApp()
    app.run()

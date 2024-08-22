from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string("""
<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Home Screen'

<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Menu Screen'

<ProfileScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Profile Screen'

<MyButton>:
    canvas.before:
        Color:
            rgba: self.background_color if not self.is_pressed else self.pressed_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.radius]

    background_color: 0, 0.5, 0.7, 1  # Tugma fon rangi
    pressed_color: 1, 0, 0, 1  # Tugma bosilgandagi rang
    radius: 15  # Tugma radiusi

    on_press:
        self.is_pressed = True
    on_release:
        self.is_pressed = False
""")

class HomeScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class MyButton(Button):
    is_pressed = False
    radius = 20

class BottomBar(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.screen_manager = screen_manager
        # Home tugmasi
        self.add_widget(MyButton(text='Home', on_press=self.switch_to_home))
        # Menu tugmasi
        self.add_widget(MyButton(text='Menu', on_press=self.switch_to_menu))
        # Profile tugmasi
        self.add_widget(MyButton(text='Profile', on_press=self.switch_to_profile))

    def switch_to_home(self, instance):
        self.screen_manager.current = 'home'

    def switch_to_menu(self, instance):
        self.screen_manager.current = 'menu'

    def switch_to_profile(self, instance):
        self.screen_manager.current = 'profile'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ProfileScreen(name='profile'))

        root = BoxLayout(orientation='vertical')
        root.add_widget(sm)
        root.add_widget(BottomBar(screen_manager=sm, size_hint_y=0.1))

        return root

if __name__ == '__main__':
    MyApp().run()

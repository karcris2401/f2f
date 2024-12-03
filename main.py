from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.swipe_screen import SwipeScreen
from screens.secret_admirer import SecretAdmirerScreen
from screens.quiz_screen import QuizScreen

class F2FApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SwipeScreen(name='swipe'))
        sm.add_widget(SecretAdmirerScreen(name='secret_admirer'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

if __name__ == '__main__':
    F2FApp().run()

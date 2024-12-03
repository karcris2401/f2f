from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.correct_answer = 1

    def submit_answer(self, answer):
        if answer == self.correct_answer:
            self.play_sound('assets/sounds/correct.mp3')
            self.ids.question_label.text = "¡Correcto! Puedes chatear."
        else:
            self.play_sound('assets/sounds/wrong.mp3')
            self.ids.question_label.text = "Incorrecto. Intenta de nuevo."

    def play_sound(self, path):
        sound = SoundLoader.load(path)
        if sound:
            sound.play()

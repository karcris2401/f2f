from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader

class SecretAdmirerScreen(Screen):
    def send_sticker(self):
        self.play_sound('assets/sounds/sticker.mp3')
        self.ids.sticker_preview.opacity = 1

    def play_sound(self, path):
        sound = SoundLoader.load(path)
        if sound:
            sound.play()

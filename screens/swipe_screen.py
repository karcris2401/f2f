from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.clock import Clock

class SwipeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profiles = [
            {'image': 'assets/profiles/user1.jpg', 'info': 'Usuario 1: Amante del arte.'},
            {'image': 'assets/profiles/user2.jpg', 'info': 'Usuario 2: Aventurero.'},
            {'image': 'assets/profiles/user3.jpg', 'info': 'Usuario 3: Amante de los libros.'},
        ]
        self.current_profile = 0
        Clock.schedule_once(self.load_profile)

    def load_profile(self, *args):
        if self.current_profile < len(self.profiles):
            self.ids.profile_image.source = self.profiles[self.current_profile]['image']
            self.ids.profile_info.text = self.profiles[self.current_profile]['info']
            self.ids.profile_image.opacity = 1
        else:
            self.ids.profile_info.text = "No hay más perfiles disponibles."

    def on_swipe_right(self):
        self.play_sound('assets/sounds/like.mp3')
        self.animate_profile()
        self.next_profile()

    def on_swipe_left(self):
        self.play_sound('assets/sounds/dislike.mp3')
        self.animate_profile()
        self.next_profile()

    def animate_profile(self):
        anim = Animation(opacity=0, duration=0.5)
        anim.start(self.ids.profile_image)

    def next_profile(self):
        self.current_profile += 1
        Clock.schedule_once(self.load_profile, 0.5)

    def play_sound(self, path):
        sound = SoundLoader.load(path)
        if sound:
            sound.play()

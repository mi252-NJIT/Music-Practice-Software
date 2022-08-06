from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, ClockEvent
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from winsound import Beep
import time

# Create all the screens for the program
class MainMenuWindow(Screen):
    pass

class ModeSelectionWindow(Screen):
    pass

class MetronomeWindow(Screen):
    # Initialize metronome sounds and necessary variables for triggering the metronome
    strong_beat = SoundLoader.load('sounds/metronome_strong.wav')
    metronome_event: ClockEvent
    tempo = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MetronomeWindow, self).__init__(**kwargs)

        # Set the metronome to be off by default
        self.metronome_active = False
        self.metronome_event = False

    def play_metronome_sound(self, dt):
        # Play the metronome sound clip
        self.strong_beat.play()

    def toggle_metronome(self):
        # Change metronome state from either off to on or on to off
        self.metronome_active = not self.metronome_active
        
        if self.metronome_active:
            # Start the metronome if it was turned on
            self.metronome_event = Clock.schedule_interval(self.play_metronome_sound, 60.0 / self.tempo.value)
        else:
            # Stop the metronome otherwise
            self.metronome_event.cancel()
    pass

    def close_metronome(self):
        # Set the metronome to the off state, and stop the sound from playing if necessary
        self.metronome_active = False

        if self.metronome_event:
            self.metronome_event.cancel()

class MidiWindow(Screen):
    pass

class OptionsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MusicApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuWindow())
        sm.add_widget(ModeSelectionWindow())
        sm.add_widget(MetronomeWindow())
        sm.add_widget(MidiWindow())
        sm.add_widget(OptionsWindow())

        return sm

if __name__ == "__main__":
    MusicApp().run()
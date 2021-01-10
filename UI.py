from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

# Create all the screens for the program
class MainMenuWindow(Screen):
    pass

class ModeSelectionWindow(Screen):
    pass

class MetronomeWindow(Screen):
    pass

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
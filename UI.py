from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class UIGrid(GridLayout):
    def __init__(self, **kwargs):
        super(UIGrid, self).__init__(**kwargs)
        self.cols = 3
    ##Creates labels and buttons for the window:
        self.programNameLabel = Label(text="Music Practice Software")
        self.playButton = Button(text="Play", font_size=40)
        self.optionsButton = Button(text="Options", font_size=40)
    ##Adds all of the created labels and buttons to the window:
        self.add_widget(self.programNameLabel)
        self.add_widget(self.playButton)
        self.add_widget(self.optionsButton)
        







class MusicApp(App):
    def build(self):
        return UIGrid()



if __name__ == "__main__":
    MusicApp().run()

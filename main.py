from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class JarvisInterface(App):
    def build(self):
        # Configuration pour le mode "Fantôme" au premier plan
        Window.borderless = True
        return Label(text='[ J.A.R.V.I.S. ACTIVE ]', font_size='30sp', color=(0, 1, 1, 1))

if __name__ == '__main__':
    JarvisInterface().run()

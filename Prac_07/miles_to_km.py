"""
CP1404/CP5632 Practical
Convert Miles to km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Milestokm(App):
    """ Milestokm is a Kivy App for converting miles to km """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.6
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, addon, value):
        value += addon
        self.root.ids.input_number.text = str(value)


Milestokm().run()

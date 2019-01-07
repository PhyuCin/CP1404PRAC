from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NamesApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["James", "Lauran", "Kerry", "Bruce"]

    def build(self):
        """ build Kivy app from the kv file """
        self.title = "Names"
        self.root = Builder.load_file('names.kv')
        self.display_name_labels()
        return self.root

    def display_name_labels(self):
        """Create labels from names and add them to the GUI."""
        for name in self.names:
            # create a label for each name
            self.root.add_widget(Label(text=name))


NamesApp().run()

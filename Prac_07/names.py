from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Milestokm(App):
    """Display names"""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyra", "Oren Ochre", "James Adams", "Suzy Bae"]

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Names"
        self.root = Builder.load_file('names.kv')
        return self.root

    def display_names(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            self.root.ids.display_name.text = name
            temp_label = Label(text=name, id=name)
            temp_label.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)
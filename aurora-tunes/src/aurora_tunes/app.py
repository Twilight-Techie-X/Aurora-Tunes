"""
Music player built in Python's Beeware.
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from gui.main_window import MainWindow


class AuroraTunes(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = MainWindow()
        self.main_window.show()


def main():
    return AuroraTunes()

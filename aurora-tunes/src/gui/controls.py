import toga
from toga.style import Pack

class Controls(toga.Box):
    def __init__(self, play_callback, pause_callback, stop_callback):
        super().__init__(style=Pack(direction='column', alignment='center'))
        self.add(
            toga.Button('Play', on_press=play_callback, style=Pack(padding=5)),
            toga.Button('Pause', on_press=pause_callback, style=Pack(padding=5)),
            toga.Button('Stop', on_press=stop_callback, style=Pack(padding=5))
        )

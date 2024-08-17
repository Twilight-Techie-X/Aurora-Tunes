import toga
from toga.style import Pack
from logic.audio import AudioPlayer
from gui.controls import Controls

class MainWindow(toga.MainWindow):
    def __init__(self):
        super().__init__(title='Aurora Tunes')
        self.audio_player = AudioPlayer()  # Initialize AudioPlayer
        self.selected_track = None

        self.controls = Controls(
            play_callback=self.play_music,
            pause_callback=self.pause_music,
            stop_callback=self.stop_music
        )
        self.volume_label = toga.Label('Volume: 50', style=Pack(padding=5))
        self.increase_volume_button = toga.Button('Increase Volume', on_press=self.increase_volume, style=Pack(padding=5))
        self.decrease_volume_button = toga.Button('Decrease Volume', on_press=self.decrease_volume, style=Pack(padding=5))
        self.progress_bar = toga.ProgressBar(style=Pack(padding=5))

        self.content = toga.Box(
            children=[
                toga.Button('Select File', on_press=self.load_music, style=Pack(padding=5)),
                self.controls,
                self.volume_label,
                self.increase_volume_button,
                self.decrease_volume_button,
                self.progress_bar,
            ],
            style=Pack(direction='column', alignment='center')
        )

    async def load_music(self, widget):
        # Open a file dialog to select a track
        file_paths = await self.open_file_dialog(title="Select a Music File?", multiple_select=True)
        if file_paths:
            self.set_selected_track(file_paths[0])  # Use the first file in the list

    def play_music(self, widget):
        if self.selected_track:
            self.audio_player.play(self.selected_track)
    
    def pause_music(self, widget):
        self.audio_player.pause()
    
    def stop_music(self, widget):
        self.audio_player.stop()

    def set_selected_track(self, file_path):
        self.selected_track = file_path

    def increase_volume(self, widget):
        current_volume = self.audio_player.get_volume()
        new_volume = min(current_volume + 10, 100)  # Increase by 10, max volume 100
        self.audio_player.set_volume(new_volume)
        self.volume_label.text = f'Volume: {new_volume}'

    def decrease_volume(self, widget):
        current_volume = self.audio_player.get_volume()
        new_volume = max(current_volume - 10, 0)  # Decrease by 10, min volume 0
        self.audio_player.set_volume(new_volume)
        self.volume_label.text = f'Volume: {new_volume}'

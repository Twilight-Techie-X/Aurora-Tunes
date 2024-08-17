class Settings:
    def __init__(self):
        self.volume = 50
        self.play_mode = 'normal'

    def set_volume(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume

    def set_play_mode(self, mode):
        self.play_mode = mode

    def get_play_mode(self):
        return self.play_mode

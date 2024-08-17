class PlaylistManager:
    def __init__(self):
        self.playlist = []
        self.current_index = 0

    def add_track(self, track):
        self.playlist.append(track)

    def remove_track(self, track):
        if track in self.playlist:
            self.playlist.remove(track)

    def get_current_track(self):
        if self.playlist:
            return self.playlist[self.current_index]
        return None

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        return self.get_current_track()

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        return self.get_current_track()

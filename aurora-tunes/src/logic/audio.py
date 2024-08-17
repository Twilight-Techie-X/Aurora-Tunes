import pygame

class AudioPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.track = None
        self.paused_position = 0

    def play(self, track):
        if self.track != track:
            pygame.mixer.music.load(track)
            self.track = track
            self.paused_position = 0  # Reset position for a new track
        
        if self.paused_position > 0:
            pygame.mixer.music.play(start=self.paused_position)
        else:
            pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            self.paused_position = pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
            pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()
        self.paused_position = 0  # Reset position

    def is_playing(self):
        return pygame.mixer.music.get_busy()
    
    def get_volume(self):
        return int(self.volume * 100)  # Convert back to a scale of 0 to 100

    def set_volume(self, volume):
        # Volume should be between 0.0 and 1.0
        if 0 <= volume <= 100:
            self.volume = volume / 100  # Convert to a scale of 0.0 to 1.0
            pygame.mixer.music.set_volume(volume)
        else:
            print("Volume must be between 0.0 and 1.0")
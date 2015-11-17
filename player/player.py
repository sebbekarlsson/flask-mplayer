import threading
import os
import pygame
import time


class Player (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dir = 'flaskr/static/music'
        self.songs = []
        pygame.mixer.init()

    def collect_songs(self):
        for subdir, dirs, files in os.walk(self.dir):
            for file in files:
                full_name = self.dir + '/' + file
                fname, file_extension = os.path.splitext(full_name)

                if 'mp3' in file_extension:
                    self.songs.append(full_name)
                else:
                    print('SKIPPING {file}'.format(file=file))

    def play_list(self):
        while len(self.songs) > 0:
            for song in self.songs:

                if pygame.mixer.music.get_busy() == True:
                    break

                print('RIGHT NOW PLAYING: {song}'.format(song=song))
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                self.songs.remove(song)

    def run(self):
        while True:
            self.collect_songs()
            self.play_list()
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
                self.songs.append(full_name)
                print(full_name)

    def play_list(self):
        while True:
            for song in self.songs:

                if pygame.mixer.music.get_busy() == True:
                    break

                print('RIGHT NOW PLAYING: {song}'.format(song=song))
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                self.songs.remove(song)

    def run(self):
        self.collect_songs()
        self.play_list()
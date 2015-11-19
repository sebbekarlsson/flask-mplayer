import threading
import os
import pygame
import time
from flaskr.models import Song, sess
from functions.songs import get_all_songs
from random import shuffle


class Player (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dir = 'flaskr/static/music'
        self.songs = []
        pygame.mixer.init()

    def collect_songs(self):
        self.songs = get_all_songs()
        shuffle(self.songs)

    def play_list(self):
        for song in self.songs:
            try:
                full_name = self.dir + '/' + song.file
                fname, file_extension = os.path.splitext(full_name)

                pygame.mixer.music.load(full_name)
                pygame.mixer.music.play()


                while pygame.mixer.music.get_busy() or 'mp3' not in file_extension:
                    song.playing = 1
                    sess.commit()
                    sess.flush()

                    time.sleep(3)


                song.playing = 0
                sess.commit()
                sess.flush()

                self.songs.remove(song)
            except:
                pass

    def run(self):
        while True:
            if len(self.songs) > 0:
                self.play_list()
            else:
                self.collect_songs()
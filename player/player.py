import threading
import os
import time
from flaskr.models import Song, sess
from functions.songs import get_all_songs
from random import shuffle
from pymplay.MusicPlayer import MusicPlayer


class Player (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dir = 'flaskr/static/music'
        self.songs = []
        self.player = MusicPlayer()

    def collect_songs(self):
        self.songs = get_all_songs()
        shuffle(self.songs)

    def play_list(self):
        for song in self.songs:
            full_name = self.dir + '/' + song.file
            fname, file_extension = os.path.splitext(full_name)

            print('PLAYING: {song}'.format(song=full_name))
            self.player.play_audio(full_name)

            self.songs.remove(song)

    def run(self):
        while True:
            self.collect_songs()
            self.play_list()
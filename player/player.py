import threading
import os
import pygame
import time
from flaskr.models import Song, sess


class Player (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dir = 'flaskr/static/music'
        self.songs = []
        pygame.mixer.init()

    def collect_songs(self):
        self.songs = db_songs = sess.query(Song).all()

    def play_list(self):
        for song in self.songs:

            full_name = self.dir + '/' + song.file
            fname, file_extension = os.path.splitext(full_name)

            print('RIGHT NOW PLAYING: {song}'.format(song=song.title))
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

    def run(self):
        while True:
            if len(self.songs) > 0:
                self.play_list()
            else:
                self.collect_songs()
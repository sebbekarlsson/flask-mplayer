from player.player import Player
from flaskr.models import sess
from functions.songs import get_all_songs


for song in get_all_songs():
    song.playing = 0
    sess.commit()


player = Player()
player.start()

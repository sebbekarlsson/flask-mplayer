from flaskr.models import sess, Song


def get_all_songs():
    return sess.query(Song).order_by(Song.id).all()

def get_playing_song():
    return sess.query(Song).filter(Song.playing==1).first()
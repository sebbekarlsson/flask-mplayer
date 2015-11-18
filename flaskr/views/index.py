from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flaskr.models import sess, Song
from functions.songs import get_all_songs, get_playing_song


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def _index():
    songs = get_all_songs()
    current_song = get_playing_song()
    return render_template('index.html', songs=songs, current_song=current_song)
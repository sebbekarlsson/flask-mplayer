from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flaskr.models import sess, Song


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def _index():
    song = sess.query(Song).filter(Song.playing==1).first()
    return render_template('index.html', song=song)
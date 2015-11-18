from flask import Blueprint, render_template, abort, url_for, request
from jinja2 import TemplateNotFound
import os
from flaskr.models import Song
from flaskr.models import sess


action = Blueprint('action', __name__,
                        template_folder='templates')

@action.route('/action/<act>', methods=['POST','GET'])
def _action(act):

    if act == 'delete':
        song_id = request.form['id']
        song = sess.query(Song).filter(Song.id==song_id).first()


        os.remove(os.path.dirname(os.path.dirname(__file__)) + '/static/music/{file}'.format(file=song.file))

        sess.delete(song)
        sess.commit()

        return 'ok'

        James_Bay_-Scars-_(Acoustic).mp3
        James_Bay_-Scars-_Acoustic.mp3

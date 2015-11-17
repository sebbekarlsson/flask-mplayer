from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from flask_wtf.file import FileField
from werkzeug import secure_filename
import os
from flaskr.models import Song
from flaskr.models import sess


upload = Blueprint('upload', __name__,
                        template_folder='templates')

class SongForm(Form):
    artist = StringField('Artist', [validators.Required()])
    title = StringField('Title', [validators.Required()])
    song = FileField('Your mp3 file', [validators.Required()])
    submit = SubmitField('Upload')

@upload.route('/upload', methods=['POST','GET'])
def _upload():
    form = SongForm(csrf_enabled=False)

    error = None

    if form.validate_on_submit():
        filename = secure_filename(form.song.data.filename)
        fname, file_extension = os.path.splitext(form.song.data.filename)
        if not 'mp3' in file_extension:
            error = 'Must be mp3'
        else:
            form.song.data.save('flaskr/static/music/' + filename)

            song = Song(artist=form.artist.data, title=form.title.data, file=form.song.data.filename)
            sess.add(song)
            sess.commit()
    else:
        filename = None
        error = None

    return render_template('upload.html', error=error, filename=filename, form=form)
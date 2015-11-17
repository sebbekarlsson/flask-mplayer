from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from flask_wtf.file import FileField
from werkzeug import secure_filename
import os
from flaskr.models import Song
from flaskr.models import sess


manage = Blueprint('manage', __name__,
                        template_folder='templates')

@manage.route('/manage', methods=['POST','GET'])
def _manage():

    songs = sess.query(Song)

    return render_template('manage.html', songs=songs)
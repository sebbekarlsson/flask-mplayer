from flask import Flask
from flaskr.views.index import index
from flaskr.views.upload import upload
from flaskr.models import initialize_database


app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(upload)

def run():
    initialize_database()
    app.run(debug=True)
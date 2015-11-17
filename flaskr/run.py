from flask import Flask
from flaskr.views.index import index
from flaskr.models import initialize_database


app = Flask(__name__)
app.register_blueprint(index)

def run():
    initialize_database()
    app.run(debug=True)
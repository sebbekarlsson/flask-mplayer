from flask import Flask
from flaskr.views.index import index


app = Flask(__name__)
app.register_blueprint(index)

def run():
    app.run(debug=True)
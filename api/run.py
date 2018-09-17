from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from app import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

app.run(host='0.0.0.0', debug=True)
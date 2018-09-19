from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from app import api

app = Flask(__name__)
app.url_map.strict_slashes = False
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
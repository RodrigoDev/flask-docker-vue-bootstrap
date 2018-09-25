from flask import Flask
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix

from app import blueprint

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
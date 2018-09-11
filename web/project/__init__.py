from flask import Flask, jsonify
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

app = Flask(__name__)
csrf = CSRFProtect(app)
CORS(app)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from project import views

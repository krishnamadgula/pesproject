from flask import Flask
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('specifications')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'templogin.html'
import app
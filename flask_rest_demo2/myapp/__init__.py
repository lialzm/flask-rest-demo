from flask import Flask

app = Flask(__name__)

from myapp.user.views import user_blueprint

app.register_blueprint(user_blueprint)
from flask import request, jsonify, Blueprint, abort

user_blueprint = Blueprint('user', __name__,url_prefix='/user')
 
@user_blueprint.route('/')
def home():
    return "Welcome to the library Home."
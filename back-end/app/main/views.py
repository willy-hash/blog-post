from flask import jsonify
from . import main
from ..models import Blog, User
from .. import db

@main.route('/', methods=['GET'])
def index():

    user1 = User.query.first()

    blogs = [{'id' : user.id , 'Blog title' : user.title} for user in user1.blogs]

    return jsonify({
        'id' : user1.id,
        'nombre' : user1.name,
        'email' : user1.email,
        'blogs' : blogs
    })
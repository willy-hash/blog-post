from flask import jsonify
from . import main
from ..models import Blog, User
from .. import db

@main.route('/', methods=['GET'])
def index():

    blog1 = Blog.query.first()

    return jsonify({
        "id": blog1.id,
        "title": blog1.title,
        "content": blog1.content,
        "image": blog1.image,
        "category": blog1.category,
        "punctuation": blog1.punctuation,
        "views": blog1.views,
        "summary": blog1.summary,
        "created_at": blog1.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": blog1.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        "author_id": blog1.author_id
    })
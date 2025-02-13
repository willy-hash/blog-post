from flask import jsonify
from . import main
from ..models import Blog, User, Comment
from .. import db

def get_comments_blog(id_blog):
    try:
        comments = Comment.query.filter_by(blog_id=id_blog).all()
    except Exception as e:
        return f"Error to connect DB - {str(e)}"

    return [x.comment for x in comments]

@main.route('/blogs', methods=['GET'])
def index():

    try:
        query_blogs = Blog.query.all()
    except Exception as e:
        return f"Error to connect DB - {str(e)}"

    blogs = [{
        "id": blog1.id,
        "title": blog1.title,
        "content": blog1.content,
        "image": blog1.image,
        "category": blog1.category,
        "punctuation": blog1.punctuation,
        "views": blog1.views,
        "summary": blog1.summary,
        "comments" : get_comments_blog(blog1.id),
        "created_at": blog1.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": blog1.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        "author": blog1.author.name
    }
    for blog1 in query_blogs
    ]

    return blogs


from . import db
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(64), nullable=False)
    punctuation = db.Column(db.Integer)
    views = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    author = db.relationship("User", back_populates="blogs")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=False)

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)


class User(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    blogs = db.relationship("Blog", back_populates="author")
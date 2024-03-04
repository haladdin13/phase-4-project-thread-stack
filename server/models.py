from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    tier = db.Column(db.Integer)
    user_avatar = db.Column(db.String)
    socials = db.Column(db.String)


    def __repr__(self):
        return f" User_name: {self.user_name} | Email: {self.email} | Tier: {self.tier} | Avatar: {self.user_avatar} | Socials: {self.socials}"


class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    thread_id = db.Column(db.Integer, db.ForeignKey("threads.id"))

    def __repr__(self):
        return f" UserID: {self.user_id} | ThreadID: {self.thread_id}"
    

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f" Category_name: {self.category_name} | Description: {self.description}"

class Thread(db.Model, SerializerMixin):
    __tablename__ = 'threads'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    likes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    edited_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f" Title: {self.title} | Content: {self.content} | Likes: {self.likes} | Created: {self.created_at} | Edited: {self.edited_at}"

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    thread_id = db.Column(db.Integer, db.ForeignKey('threads.id'))
    likes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    edited_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f" Content: {self.content} | User_ID: {self.user_id} | Thread_id: {self.thread_id} | likes: {self.likes} | Created: {self.created_at} | Edited: {self.edited_at}"
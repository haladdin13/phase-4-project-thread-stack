from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    tier = db.Column(db.Integer)
    user_avatar = db.Column(db.String)
    posts = db.Column(db.String)
    region = db.Column(db.String)


    def __repr__(self):
        return f" User_name: {self.user_name} | Tier: {self.tier} | Avatar: {self.user_avatar} | Posts: {self.posts} | Region: {self.region}"


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer)
    thread_id = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f" Content: {self.content} | User_ID: {self.user_id} | Thread_id: {self.thread_id} | likes: {self.likes}"
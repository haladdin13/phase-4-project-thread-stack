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


class Dashboard(db.Model, SerializerMixin):
    __tablename__ = 'dashboards'
    id = db.Column(db.Integer, primary_key=True)
    dashboard_titles = db.Column(db.String, unique=True, nullable=False)
    recent_threads_id = db.Column(db.Integer)
    saved_threads_id = db.Column(db.Integer)

    def __repr__(self):
        return f" Forum_titles: {self.dashboard_titles} | Recent_threads_id: {self.recent_threads_id} | Saved_threads_id: {self.saved_threads_id}"
    

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    category_name = db.Column(db.String)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboards.id'))
    description = db.Column(db.String)

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
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f" Title: {self.title} | Content: {self.content} | Likes: {self.likes} | Created: {self.created_at} | Updated: {self.updated_at}"

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    thread_id = db.Column(db.Integer, db.ForeignKey('threads.id'))
    likes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f" Content: {self.content} | User_ID: {self.user_id} | Thread_id: {self.thread_id} | likes: {self.likes} | Created: {self.created_at} | Updated: {self.updated_at}"
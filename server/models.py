from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

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

    #RELATIONSHIPS

    #SERIALIZATION RULES

    #ADD VALIDATIONS

    def __repr__(self):
        return f" User_name: {self.user_name} | Email: {self.email} | Tier: {self.tier} | Avatar: {self.user_avatar} | Socials: {self.socials}"


class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    thread_id = db.Column(db.Integer, db.ForeignKey("threads.id"))

    def __repr__(self):
        return f" UserID: {self.user_id} | ThreadID: {self.thread_id}"
    
    #RELATIONSHIPS

    user = db.relationship('User', back_populates='favorites')
    thread = db.relationship('Thread', back_populates='favorites')

    #SERIALIZATION RULES

    serialize_rules = ('-user.favorites', '-thread.favorites')

    #ADD VALIDATIONS


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f" Category_name: {self.category_name} | Description: {self.description}"


    #RELATIONSHIPS

    users = db.relationship('User', back_populates = 'category')
    threads = db.relationship('Thread', back_populates = 'category')

    #SERIALIZATION RULES

    serialize_rules = ('-users.category', '-threads.category')

    #ADD VALIDATIONS

    @validates('category_name')
    def validate_category_name(self, key, category_name):
        if isinstance(category_name, str) and len(category_name) > 2:
            return category_name
        else:
            raise ValueError('Category name must be a string at least 3 characters long')
    
    @validates('description')
    def validate_description(self, key, description):
        if isinstance(description, str) and len(description) > 5:
            return description
        else:
            raise ValueError('Description must be a string at least 6 characters long')


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

    #RELATIONSHIPS

    #SERIALIZATION RULES

    #ADD VALIDATIONS


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
    
    #RELATIONSHIPS

    user = db.relationship('User', back_poplulates = 'posts')
    thread = db.relationship('Thread', back_populates = 'posts')

    #SERIALIZATION RULES

    serialize_rules = ('-user.posts', '-thread.posts')

    #ADD VALIDATIONS

    @validates('content')
    def validate_content(self, key, content):
        if isinstance(content, str) and len(content) > 5:
            return content
        else:
            raise ValueError('Content must be a string at least 6 characters long')
        
    
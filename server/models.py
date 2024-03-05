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
    posts = db.relationship('Post', back_populates = 'user')
    favorites = db.relationship('Favorite', back_populates = 'user')
    categories = db.relationship('Category', back_populates = 'user')

    #SERIALIZATION RULES
    serialize_rules = ('-posts.user', '-favorites.user', '-categories.user')

    #ADD VALIDATIONS

    @validates('user_name')
    def validate_user_name(self, key, user_name):
        if isinstance(user_name, str) and len(user_name) > 5:
            return user_name
        else:
            raise ValueError("Username must be longer than 5 characters")
        
    @validates('email')
    def validate_email(self, key, email):
        if isinstance(email, str) and len(email) > 5:
            return email
        else:
            raise ValueError("Email must be longer than 5 characters")
        
    @validates('password')
    def validate_password(self, key, password):
        if isinstance(password, str) and len(password) > 5:
            return password
        else:
            raise ValueError("Password must be longer than 5 characters")
        
    @validates('user_avatar')
    def validate_user_avatar(self, key, user_avatar):
        if isinstance(user_avatar, str):
            return user_avatar
        else:
            raise ValueError("User avatar must be of type (.jpg)")
        
    @validates('socials')
    def validate_socials(self, key, socials):
        if isinstance(socials, str):
            return socials
        else:
            raise ValueError("Please include Socials.")

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

    user = db.relationship('User', back_populates = 'categories')
    threads = db.relationship('Thread', back_populates = 'category')

    #SERIALIZATION RULES

    serialize_rules = ('-user.categories', '-threads.category', '-user.favorites', '-threads.favorites', '-threads.posts')

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
    thread_title = db.Column(db.String)
    thread_content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    likes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    edited_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f" Title: {self.thread_title} | Content: {self.thread_content} | Likes: {self.likes} | Created: {self.created_at} | Edited: {self.edited_at}"

    #RELATIONSHIPS
    category = db.relationship('Category', back_populates = 'threads')
    favorites = db.relationship('Favorite', back_populates = 'thread')
    posts = db.relationship('Post', back_populates = 'thread')

    #SERIALIZATION RULES
    serialize_rules = ('-category.threads', '-favorites.thread', '-posts.thread')

    #ADD VALIDATIONS
    @validates('thread_title')
    def title(self, key, thread_title):
        if isinstance(thread_title, str) and len(thread_title) > 5:
            return thread_title
        else:
            raise ValueError('Title must be longer than 5 characters')
        
    @validates('thread_content')
    def content(self, key, thread_content):
        if isinstance(thread_content, str) and len(thread_content) > 5:
            return thread_content
        else:
            raise ValueError("Content must be greater than 5 characters")
        
    


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

    user = db.relationship('User', back_populates = 'posts')
    thread = db.relationship('Thread', back_populates = 'posts')

    #SERIALIZATION RULES

    serialize_rules = ('-user.posts', '-thread.posts', '-user.categories', '-user.favorites', '-thread.category', '-thread.favorites')

    #ADD VALIDATIONS

    @validates('content')
    def validate_content(self, key, content):
        if isinstance(content, str) and len(content) > 5:
            return content
        else:
            raise ValueError('Content must be a string at least 6 characters long')
        
    
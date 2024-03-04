from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.int, primary_key=True)
    user_name = db.Column(db.str, unique=True)
    password = db.Column(db.str)
    tier = db.Column(db.int)
    user_avatar = db.Column(db.str)
    posts = db.Column(db.str)
    region = db.Column(db.str)


    def __repr__(self):
        return f" User_name: {self.user_name} | Tier: {self.tier} | Avatar: {self.user_avatar} | Posts: {self.posts} | Region: {self.region}"



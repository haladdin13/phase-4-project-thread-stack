#!/usr/bin/env python3

# Standard library imports
from models import Category, User, Post, Favorite, Thread

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


#Get All Category Routes
@app.route('/categories', methods=['GET'])
def categories():
    categories_list = [category.to_dict() for category in Category.objects.all()]
    response = make_response(categories_list, 200)

    return response


#Get All Posts
@app.route('/posts', methods=['GET'])
def posts():
    posts_list = [post.to_dict() for post in Post.objects.all()]
    response = make_response(posts_list, 200)

    return response

#Get Posts By ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def post_by_id(post_id):
    post = Post.query.filter(Post.id == post_id).first()
    response = make_response(post.to_dict(), 200)

    return response


#Get All Favorites
@app.route('/favorites', methods=['GET'])
def favorites(request):
    favorites_list = [favorite.to_dict() for favorite in Favorite.objects.all()]
    response = make_response(favorites_list, 200)

    return response

#Get Favorites By ID
@app.route('/favorites/<int:favorite_id>', methods=['GET'])
def favorite_by_id(favorite_id):
    favorite = Favorite.query.filter(Favorite.id == favorite_id).first()
    response = make_response(favorite.to_dict(), 200)

    return response

    

@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    users_dict = [user.to_dict() for user in users]

    response = make_response(
        users_dict,
        200
    )
    return response



@app.route('/users/<id:int>', methods=['GET'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()
    user_dict = user.to_dict()

    response = make_response(
        user_dict,
        200
    )

    return response



@app.route('/threads', methods=['GET'])
def threads():
    threads = Thread.query.all()
    threads_dict =  [thread.to_dict() for thread in threads]

    response = make_response(
        threads_dict,
        200
    )

    return response


@app.route('threads/<id:int>', methods=['GET'])
def thread_by_id(id):
    thread = User.query.filter(Thread.id == id).first()
    thread_dict = thread.to_dict()

    response = make_response(
        thread_dict,
        200
    )

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

#testing
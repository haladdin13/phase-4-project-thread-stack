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
    make_response = (categories_list, 200)

    return make_response

    

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
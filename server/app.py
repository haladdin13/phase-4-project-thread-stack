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
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    
    if request.method == 'GET':
    
        categories_list = [category.to_dict() for category in Category.query.all()]
        response = make_response(categories_list, 200)

    elif request.method == 'POST':
        new_category = Category(
            category_name = request.json['category_name'],
            description = request.json['description'],
            user_id = request.json['user_id']
        )
        db.session.add(new_category)
        db.session.commit()
        response = make_response(new_category.to_dict(), 201)
    else:
        response = make_response({'message': 'Method not allowed'}, 405)
    
    return response
#Get Category By ID
    
@app.route('/categories/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def category_by_id(id):
    category = Category.query.filter(Category.id == id).first()
    if category:
        if request.method == 'GET':
            category_dict = category.to_dict()

            response = make_response(category_dict, 200)
        elif request.method == 'PATCH':
            
            try:
                form_data = request.get_json()

                for attr in form_data:
                    setattr(category, attr, form_data[attr])

                db.session.commit()

                response = make_response(category.to_dict(), 202)
            except ValueError:
                response = make_response({'errors': ['Validation Errors']}, 400)
        elif request.method == 'DELETE':
            assoc_threads = Thread.query.filter(Thread.category_id == id).all()
            for assoc_thread in assoc_threads:
                db.session.delete(assoc_thread)

                db.session.delete(category)

                db.session.commit()
                response = make_response({}, 204)

            
            # assoc_posts = Post.query.filter(Post.category_id == id).all()
            # for assoc_post in assoc_posts:
            #     db.session.delete(assoc_post)

            #     db.session.delete(category)

            #     db.session.commit()
            #     response = make_response({}, 204)
            db.session.delete(category)
            db.session.commit()
            response = make_response('', 204)
    else:
        response = make_response(
            {'message': 'Method not allowed'}, 405
        )
    return response



#Get All Posts
@app.route('/posts', methods=['GET'])
def posts():
    posts_list = [post.to_dict() for post in Post.query.all()]
    response = make_response(posts_list, 200)

    return response

#Get Posts By ID
@app.route('/posts/<int:id>', methods=['GET'])
def post_by_id(id):
    post = Post.query.filter(Post.id == id).first()
    response = make_response(post.to_dict(), 200)

    return response


#Get All Favorites
@app.route('/favorites', methods=['GET'])
def favorites():
    favorites_list = [favorite.to_dict() for favorite in Favorite.query.all()]
    response = make_response(favorites_list, 200)

    return response

#Get Favorites By ID
@app.route('/favorites/<int:id>', methods=['GET'])
def favorite_by_id(id):
    favorite = Favorite.query.filter(Favorite.id == id).first()
    response = make_response(favorite.to_dict(), 200)

    return response

    
#Get All Users
@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    users_dict = [user.to_dict() for user in users]

    response = make_response(
        users_dict,
        200
    )
    return response


#Get Users by ID
@app.route('/users/<int:id>', methods=['GET'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()
    user_dict = user.to_dict()

    response = make_response(
        user_dict,
        200
    )

    return response


#Get All Threads
@app.route('/threads', methods=['GET', 'POST'])
def threads():
    if request.method == "GET":
        threads = Thread.query.all()
        threads_dict =  [thread.to_dict() for thread in threads]

        response = make_response(
            threads_dict,
            200
        )

    elif request.method == "POST":
        new_thread = Thread(
            thread_title = request.json['thread_title'],
            thread_content = request.json['thread_content'],
            category_id = request.json['category_id'],
            likes = request.json['likes']
        )
        db.session.add(new_thread)
        db.session.commit()

        response = make_response(
            new_thread.to_dict(),
            200
        )
    else:
        response = make_response(
            {'message': 'Method is not working'},
            405
        )

    return response

#Get Threads by ID
@app.route('/threads/<int:id>', methods=['GET'])
def thread_by_id(id):
    thread = Thread.query.filter(Thread.id == id).first()
    thread_dict = thread.to_dict()

    response = make_response(
        thread_dict,
        200
    )

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

#testing
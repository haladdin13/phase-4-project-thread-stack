#!/usr/bin/env python3

# Standard library imports
from models import *

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if not user:
            return make_response(
                {'error': "Unauthorized: you must be logged in."},
                401
            )
        else:
            return make_response(
                user.to_dict(),
                200
            )

api.add_resource(CheckSession, '/check_session', endpoint='check_session')

class Signup(Resource):
    def post(self):
        json = request.get_json()
        try:
            user = User(
                user_name=json['user_name'],
                email=json['email']
            )
            user.password_hash = json['password']
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id

            return make_response(
                user.to_dict(),
                201
            )
        except Exception as e:
            return make_response(
                {'error': str(e) },
                422
            )

api.add_resource(Signup, '/signup', endpoint='signup')


class Login(Resource):
    def post(self):
        user_name = request.get_json()['user_name']

        user = User.query.filter(User.user_name == user_name).first()
        password = request.get_json()['password']

        if not user:
            response_body = {'error': 'User not found.'}
            status = 404

        else:
            if user.authenticate(password):
                session['user_id'] = user.id
                response_body = user.to_dict()
                status = 200
            else:
                response_body = {'error': 'Invalid username or password'}
                status = 401

        return make_response(response_body, status)

api.add_resource(Login, '/login', endpoint='login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}, 204

api.add_resource(Logout, '/logout', endpoint='logout')

allowed_endpoints = ['signup', 'login', 'check_session', 'categories', 'category_by_id', 'threads_by_category', 'posts', 'post_by_id', 'favorites', 'favorite_by_id', 'users', 'user_by_id', 'threads', 'thread_by_id' ]
@app.before_request
def check_if_logged_in():
    if not session.get('user_id') and request.endpoint not in allowed_endpoints:
        return {'error': 'Unauthorized'}, 401

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


# Get All Threads By Category

@app.route('/categories/<int:id>/threads', methods=['GET'])
def threads_by_category(id):
    category = Category.query.filter(Category.id == id).first()
    if category:
        thread_list = [thread.to_dict() for thread in Thread.query.filter(Thread.category_id == id).all()]
        response = make_response(thread_list, 200)
    else:
        response = make_response(
            {'message': 'Method not allowed'}, 405
        )
    return response



#Get All Posts
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
    
        post_list = [post.to_dict() for post in Post.query.all()]
        response = make_response(post_list, 200)

    elif request.method == 'POST':
        data = request.json
        new_post = Post(
            content = request.json['content'],
            user_id = request.json['user_id'],
            thread_id = request.json['thread_id']
        )
        if 'likes' in data:
            new_post.likes = data['likes']
        db.session.add(new_post)
        db.session.commit()
        response = make_response(new_post.to_dict(), 201)
    else:
        response = make_response({'message': 'Method not allowed'}, 405)
    
    return response

#Get Posts By ID
@app.route('/posts/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def post_by_id(id):
    post_query = Post.query.filter(Post.id == id).first()
    if post_query:
        if request.method == 'GET':
            post_dict = post_query.to_dict()

            response = make_response(post_dict, 200)
        elif request.method == 'PATCH':
            
            try:
                form_data = request.get_json()

                for attr in form_data:
                    setattr(post_query, attr, form_data[attr])

                db.session.commit()

                response = make_response(post_query.to_dict(), 202)
            except ValueError:
                response = make_response({'errors': ['Validation Errors']}, 400)
        elif request.method == 'DELETE':
            
            db.session.delete(post_query)
            db.session.commit()
            response = make_response('', 204)
    else:
        response = make_response(
            {'message': 'Method not allowed'}, 405
        )
    return response


#Get All Favorites
@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    favorites_list = [favorite.to_dict() for favorite in Favorite.query.all()]
    if request.method == 'GET':
        response = make_response(favorites_list, 200)
        
    elif request.method == 'POST':
        new_favorite = Favorite(
            user_id = request.json['user_id'],
            thread_id = request.json['thread_id']
        )

        db.session.add(new_favorite)
        db.session.commit()
        response = make_response(new_favorite.to_dict(), 201)
        
    else:
        response = make_response({'message': 'Method not allowed'}, 405)

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
        data = request.json
        new_thread = Thread(
            thread_title = request.json['thread_title'],
            thread_content = request.json['thread_content'],
            category_id = request.json['category_id'],
            
        )
        if 'likes' in data:
            new_thread.likes = data['likes']
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
@app.route('/threads/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def thread_by_id(id):
    thread = Thread.query.filter(Thread.id == id).first()

    if thread:
        if request.method == 'GET':

            thread_dict = thread.to_dict()

            response = make_response(
                thread_dict,
                200
            )
        elif request.method == 'PATCH':
            try:
                form_data = request.get_json()

                for attr in form_data:
                    setattr(thread, attr, form_data[attr])
                
                db.session.commit()

                response = make_response(
                    thread.to_dict(),
                    202
                )
            except ValueError:
                response = make_response(
                    {'errors': ['Validation Errors']},
                    400
                )
        elif request.method == 'DELETE':
            assoc_posts = Post.query.filter(Post.thread_id == id).all()
            for assoc_post in assoc_posts:
                db.session.delete(assoc_post)
                db.session.delete(thread)

                db.session.commit()
                response = make_response(
                    {},
                    204
                )
            db.session.delete(thread)
            db.session.commit()
            response = make_response(
                '',
                204
            )
            
        else:
            response = make_response(
                {'message': 'Invalid Method'},
                405
            )

        return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

#testing
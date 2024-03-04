#!/usr/bin/env python3

# Standard library imports
from models import Category

# Remote library imports
from flask import request
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



if __name__ == '__main__':
    app.run(port=5555, debug=True)

#testing
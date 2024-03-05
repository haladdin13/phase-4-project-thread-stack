#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Thread, Post, Category, Favorite

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        print("clearing out tables")

        User.query.delete()
        Thread.query.delete()
        Category.query.delete()
        Favorite.query.delete()
        Post.query.delete()


        print("Seeding Users Table...")


        new_user_1 = User(
        user_name = "Nuburooj",
        email = "nuburoojkhattak@gmail.com",
        password = "123456",
        tier = 10,
        user_avatar = "data:image/webp;base64,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",
        socials = "www.instagram.com/nuburooj"
        )

        db.session.add(new_user_1)
        db.session.commit()


        print("Seeding Categorys Table...")

        new_category_1 = Category(
        category_name = "Test Category",
        description = "This is the first test Category",
        user_id = new_user_1.id
        )

        db.session.add(new_category_1)
        db.session.commit()


        print("Seeding Threads Table...")

        new_thread_1 = Thread(
        thread_title = "This is the first test thread",
        thread_content = "This worked, who knew?",
        category_id = new_category_1.id,
        likes = 6

        )

        db.session.add(new_thread_1)
        db.session.commit()


        print("Seeding Posts Table...")

        new_post_1 = Post(
        content = "this is the first test post",
        user_id = new_user_1.id,
        thread_id = new_thread_1.id,
        likes = 5

        )

        db.session.add(new_post_1)
        db.session.commit()


        print("Seeding Favorites Table...")

        new_favorite_1 = Favorite(
        user_id = new_user_1.id,
        thread_id = new_thread_1.id
        )

        db.session.add(new_favorite_1)
        db.session.commit()



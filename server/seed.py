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
        
        print("clearing out tables")
        User.query.delete()
        Thread.query.delete()
        Category.query.delete()
        Favorite.query.delete()
        Post.query.delete()

        print("Seeding Users Table...")
        users = []
        for _ in range(10):  # Create 10 users
            user = User(
                user_name=fake.user_name(),
                email=fake.email(),
                password=fake.password(length=10),
                tier=randint(1, 10),
                user_avatar=fake.image_url(),
                socials=fake.url()
            )
            db.session.add(user)
            users.append(user)
        db.session.commit()

        print("Seeding Categories Table...")
        categories = []
        for _ in range(5):  # Create 5 categories
            category = Category(
                category_name=fake.word().capitalize() + " Category",
                description=fake.sentence(),
                user_id=rc(users).id
            )
            db.session.add(category)
            categories.append(category)
        db.session.commit()

        print("Seeding Threads Table...")
        threads = []
        for _ in range(20):  # Create 20 threads
            thread = Thread(
                thread_title=fake.sentence(),
                thread_content=fake.text(),
                category_id=rc(categories).id,
                likes=randint(0, 100)
            )
            db.session.add(thread)
            threads.append(thread)
        db.session.commit()

        print("Seeding Posts Table...")
        for _ in range(100):  # Create 100 posts
            post = Post(
                content=fake.text(),
                user_id=rc(users).id,
                thread_id=rc(threads).id,
                likes=randint(0, 100)
            )
            db.session.add(post)
        db.session.commit()

        print("Seeding Favorites Table...")
        for _ in range(50):  # Create 50 favorites
            favorite = Favorite(
                user_id=rc(users).id,
                thread_id=rc(threads).id
            )
            db.session.add(favorite)
        db.session.commit()

        print("Seed complete!")

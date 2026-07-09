# Mini Instagram Backend (Python CLI)

A small-scale Instagram backend simulation built in Python to learn object-oriented programming, backend design, and software development concepts.

This project currently runs as a command-line application and stores data in memory. It is being developed incrementally, with new features added over time.

## Features Implemented

- User account creation (registration)
- Duplicate username checking
- User login with password verification
- User logout
- Account deletion
- Auto-generated unique user IDs
<<<<<<< HEAD
- Create posts
- Auto-generated unique post IDs
- Track the number of posts created by each user
- In-memory user and post management using Python dictionaries
- Menu-driven command-line interface
=======
- In-memory user management using Python dictionaries
- Menu-driven command-line interface 

>>>>>>> 20b17948c6387c8d94c5cd41313c23d63df2efb3

## Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Dictionaries
- Classes and Objects
- Command-Line Interface (CLI)

## Current Project Structure

```
<<<<<<< HEAD
Instagram
backend.py
│
├── UserManager
│     ├── users {}
│     ├── next_user_id
│     ├── create_user()
│     ├── login()
│     └── delete_account()
│
├── Post
│     ├── name
│     ├── content
│     └── post_id
│
├── PostManager
│     ├── posts {}
│     ├── next_post_id
│     └── create_post()
│
├── InstagramApp
│     ├── self.users = UserManager()
│     └── self.posts = PostManager()
│
└── CLI Menu
      ├── Create Account
      ├── Login
      ├── Delete Account
      ├── Create Post
      ├── Logout
      └── Exit
=======
InstagramApp
│
├── UserManager
│   ├── User Registration
│   ├── User Login
│   ├── Delete Account
│   └── In-Memory User Storage
│
├── PostManager (Planned)
│
└── FollowManager (Planned)
```
>>>>>>> 20b17948c6387c8d94c5cd41313c23d63df2efb3

## Planned Features

- View posts
- Delete posts
- Like posts
- Comment system
- Follow /  Unfollow users
- User profiles
- Search users
- SQLite database integration
- Password hashing
- REST API using FastAPI
- Frontend integration

## Learning Goals

This project is being built to understand:

- Object-oriented design
- Backend application architecture
- Data structures in real applications
- Authentication concepts
- Database integration
- API development
- Software engineering practices

## Project Status

🚧 Work in Progress


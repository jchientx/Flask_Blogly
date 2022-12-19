"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png")

    posts = db.relationship("Post", backref="users")

    @property
    def full_name(self):
        """Return full name of the user"""
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # tags = db.relationship('Tag', secondary='posts_tags', backref='posts')

class PostTag(db.Model): # Didn't use this Model! Can be removed (and remove secondary) in this case
    """Joins together Post and Tag. Show the tag on a post."""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Tag(db.Model):
    """Tag"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship('Post', secondary='posts_tags', backref='tags') # This line relates table posts & tags
    #                     Class_want_to_relate, joined_table, table_in_this_Class


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)
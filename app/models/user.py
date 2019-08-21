from app import db
from sqlalchemy.sql import func


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(128),
        nullable=False
    )

    first_name = db.Column(
        db.String(100),
        nullable=True
    )

    last_name = db.Column(
        db.String(100),
        nullable=True
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    modified_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now()
    )
    permissions = db.relationship(
        'user_permissions',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, username, first_name, last_name, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

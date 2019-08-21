from app import db


class Permission(db.Model):

    __tablename__ = 'permissions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Permission {self.name}>'

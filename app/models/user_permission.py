from app import db


class UserPermission(db.Model):

    __tablename__ = 'user_permissions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    permission_id = db.Column(
        db.Integer,
        db.ForeignKey('permissions.id')
    )

    def __init__(self, user_id, permission_id):
        self.user_id = user_id
        self.permission_id = permission_id

    def __repr__(self):
        return (
            f'<User_id {self.user_id} - Permission_id {self.permission_ide}>'
        )

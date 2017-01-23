from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Creates a users table
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default = False)

    @property
    def password(self):
        '''
        Prevents the password from being accessed
        '''
        raise AttributeError('passwords are protected!')
    def verify_password(self):
        '''
        Compares the password with its hashed value
        '''
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User: {}>'.format(self.username)

    #setup the userloader function

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Data(db.Model):
        '''
        Creates a table to store user Data

        '''
        __tablename__ = 'data'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(60), unique=True)
        description = db.Column(db.String(200))
        employees = db.relationship('User', backref='data',
        lazy='dynamic')

        def __repr__(self):
            return '<Data: {}>'.format(self.title)

class Role(db.Model):
    '''
    Creates a role table
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users = db.relationship('User', backref='role',
    lazy='dynamic')

    def __repr__(self):
        return 'Role: {}>'.format(self.name)

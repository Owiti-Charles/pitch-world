from . import db,login_manager
from flask_login import UserMixin
from werkzeug import generate_password_hash,check_password_hash

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(255),unique = True,nullable = False)
    # email = db.Column(db.String(255),unique = True,nullable = False)
    # password = db.Column(db.String(255),nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    password = db.Column(db.String(255))
    email  = db.Column(db.String(255),unique = True,index = True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError("You can not read the password")
    @password.setter
    def set_password(self, password):
        password_hash = generate_password_hash(password)
        self.password = password_hash

    def verify_password(self, password):
        return check_password_hash(self.password,password) 

    
    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
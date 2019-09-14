from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,index = True)
    email  = db.Column(db.String(255),unique = True,index = True)
    secure_password = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError("You can not read the password")
    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    
    def __repr__(self):
        return f'User {self.username}'


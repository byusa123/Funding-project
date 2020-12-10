from . import db,login_manager
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__='users'
    id =db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(255),unique = True)
    email = db.Column(db.String(255),unique = True , index = True)
    password_secure = db.Column(db.String(255))
    image_pic_path = db.Column(db.String(255))
    posts = db.relationship('Post',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")


    @property
    def password(self):

        raise AttributeError('You cannot read the password attribute')

        
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(),primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    category = db.Column(db.String(255), index = True)
    description = db.Column(db.Text(),nullable = False)
    profile_pic_path = db.Column(db.String(255))
    content = db.Column(db.Text(),nullable = False)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'post',lazy="dynamic")

      
    def save_post(self):

        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Post {self.title}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(),primary_key = True)
    content =  db.Column(db.Text(),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    

    def __repr__(self):
        return f'Comment {self.content}'

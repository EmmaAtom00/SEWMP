from datetime import datetime
from packages import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    firstname = db.Column(db.String(120), nullable = False)
    lastname = db.Column(db.String(120), nullable = False)
    profile_img = db.Column(db.String(20), nullable = False, default = 'Default.jpg')
    password = db.Column(db.String(60), nullable = False)
    C_Task = db.relationship('create_task', backref = 'author', lazy = True)

    def __repr__(self):
        return f"user('{self.username}', '{self.email}', '{self.profile_img}')"



class create_task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    Description = db.Column(db.String(1000))
    Date_Posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self):
        return f"create_task('{self.title}', '{self.Description}', '{self.Date_Posted}')"

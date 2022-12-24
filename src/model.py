from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash

db = SQLAlchemy()


def setup_db(app, database_path):
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{database_path}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)



def db_drop_and_create_all(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.String(150),unique=True)
    user_pwd=db.Column(db.String(30))

def add_user(app,mylist):
    with app.app_context():
        for i in mylist:
            id=i
            pd=i
            new_user=User(user_id=id,user_pwd=generate_password_hash(pd,method='sha256'))
            db.session.add(new_user)
            db.session.commit()



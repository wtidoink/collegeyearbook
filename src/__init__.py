from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager,login_required
'''import csv

mylist=[]'''



DB_NAME="data.db"
def createapp()->Flask:
    app=Flask(__name__) 
    #database config
    from .model import setup_db,User,add_user
    setup_db(app,DB_NAME)
    app.config['SECRET_KEY']='adadalkdmalmdalmd'
    from .views import views
    from .auth import auth
    app.view_functions['static/images']=login_required(app.send_static_file)
    #db_drop_and_create_all(app)
    '''
    with open('new.csv','r') as csvfile:
        read=csv.reader(csvfile,delimiter=',')
        for row in read:
            mylist.append(row[0])
    print(mylist)
    add_user(app,mylist)'''
    
    #add_user(app)
    login_manager=LoginManager()
    login_manager.login_view='auth.login_to'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app



from flask import Blueprint,render_template,request,redirect,url_for,flash
from .model import User,db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_user,logout_user,login_required


auth= Blueprint('auth',__name__)

@auth.route('/',methods=['GET','POST'])
def login_to():
    if request.method=='POST':
        user_id=request.form.get('usrid')
        password=request.form.get('pwd')
        user=User.query.filter_by(user_id=user_id).first()
        if user:
            if check_password_hash(user.user_pwd,password):
                login_user(user,remember=True)  #stores data of persons loggin session(boolean)
                return redirect(url_for('views.hello_world'))
            else:
                flash('Incorrect Password')
        else:
            flash('User doesnot exist')
    return render_template('users/login.html')



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_to'))

@auth.route('/profile',methods=['GET','POST'])
@login_required
def user_profile():
    if request.method=='POST':
        user_id=request.form.get('usrid')
        password=request.form.get('pwd')
        repassword=request.form.get('repwd')
        user=User.query.filter_by(user_id=user_id).first()
        if user and check_pass(password,repassword):
            user.user_pwd=generate_password_hash(password,method='sha256')
            db.session.commit()
            flash('Successfully changed-password')
            return redirect(url_for('auth.login_to'))
        else:
            flash('Passwords dont match')

    return render_template('users/user.html')


def check_pass(p1,p2)->bool:
    return p1==p2
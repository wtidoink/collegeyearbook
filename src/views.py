from flask import Blueprint,render_template
from flask_login import login_required

views= Blueprint('views',__name__)


@views.route('/home')
@login_required
def hello_world():
    return render_template('index.html')

@views.route('/people')
@login_required
def show_people():
    return render_template('people.html')

@views.route('/timeline')
@login_required
def show_timeline():
    return render_template('timeline.html')



@views.route('/blog1')
@login_required
def show_blog1():
    return render_template('blogs/blog1.html')

@views.route('/blog2')
@login_required
def show_blog2():
    return render_template('blogs/blog2.html')

@views.route('/blog3')
@login_required
def show_blog3():
    return render_template('blogs/blog3.html')

@views.route('/blog4')
@login_required
def show_blog4():
    return render_template('blogs/blog4.html')











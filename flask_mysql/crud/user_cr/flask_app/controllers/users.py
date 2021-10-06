from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect ('/users') # redirect to show all users page

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("read.html",all_users = users) # show all users

@app.route('/user/new')
def new():
    return render_template("create.html") # the page to create new user

@app.route('/user/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users') # create and saving new users and  go back all users page


@app.route('/user/<int:user_id>/edit') # edit user
def edit(user_id):
    data ={ 
        "id":user_id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/user/<int:user_id>/show') # show singleuser 
def show(user_id):
    data ={ 
        "id":user_id
    }
    return render_template("read_one.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST']) #update users
def change():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/<int:id>/destroy') # destroy
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')

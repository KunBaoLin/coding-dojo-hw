from flask import render_template, session,redirect, request,flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree

bcrypt = Bcrypt(app)


@app.route('/') #get method, the home page
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])  #post method,, to register a new user
def register():
    is_valid = User.validate_register(request.form)
    if not is_valid:
        return redirect("/")
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(new_user)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')


@app.route("/login",methods=['POST'])   #post method . to login 
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')  
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data),trees=Tree.get_all())

@app.route('/mytrees')  
def mytrees():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id':session['user_id']
    }
    user = User.get_by_id(data)
    trees = Tree.get_user_trees(data)
    return render_template("show.html",user = user,all_trees = trees)


@app.route('/logout') # logout
def logout():
    session.clear()
    return redirect('/')

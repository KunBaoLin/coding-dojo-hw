from flask import render_template, session,flash,redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree


@app.route('/new/tree') # route to create 
def new_tree():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('creat_new.html',user=User.get_by_id(data))


@app.route('/create/tree',methods=['POST'])  #create new 
def create_tree():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tree.validate_tree(request.form):
        return redirect('/new/tree')
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "reason": request.form["reason"],
        "date_planted": request.form['date_planted'],
        "user_id": session["user_id"]
    }
    Tree.save(data)
    return redirect('/dashboard')

@app.route('/edit/tree/<int:id>') # route to edit tree
def edit_tree(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html",edit=Tree.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/tree/<int:id>',methods=['POST']) #update
def update_tree(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tree.validate_tree(request.form):
        return redirect(f'/edit/tree/{id}')
    data = {
        "id": request.form['id'],
        "name": request.form["name"],
        "location": request.form["location"],
        "reason": request.form["reason"],
        'date_planted':request.form['date_planted']
    }
    Tree.update(data)
    return redirect('/dashboard')


@app.route('/tree/<int:id>')
def show_tree(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("detail.html",tree=Tree.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/tree/<int:id>', methods = ['post']) #destroy
def destroy_tree(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Tree.destroy(data)
    return redirect('/dashboard')

from types import MethodDescriptorType
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ['post'])
def create():
    if not email.Email.is_valid(request.form):
        return redirect('/')
    else:
        flash ('The email you enter is succesful registered.')
    email.Email.save(request.form)
    return redirect ('/shows')

@app.route('/shows')
def shows():
    return render_template('results.html',emails = email.Email.get_all())

@app.route('/destroy/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    email.Email.destroy(data)
    return redirect('/shows')

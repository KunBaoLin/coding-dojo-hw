from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



@app.route('/ninjas')  #get, showing all dojo to pick and creat ninjas at dojo
def ninja():
    return render_template('ninjas.html',dojos=Dojo.get_all())   

@app.route('/ninjas/create',methods=['post']) #post, creating ninja
def create_ninja():
    Ninja.save(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

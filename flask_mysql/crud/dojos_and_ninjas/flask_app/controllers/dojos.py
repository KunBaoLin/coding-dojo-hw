from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos') # get, show all dojos
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html',all_dojos= dojos)

@app.route('/dojos/create',methods=['post']) #post create dojo
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:id>') #get, show single dojo with ninjas
def show_dojo(id):
    data={
        "id":id
    }
    return render_template('dojo_show.html',dojo=Dojo.get_one_with_ninjas(data))
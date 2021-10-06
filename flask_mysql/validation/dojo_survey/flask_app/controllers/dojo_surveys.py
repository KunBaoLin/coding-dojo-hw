from flask import render_template,request,redirect
from flask_app import app
from flask_app.models.dojo_survey import Dojo_survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_survey', methods= ['POST'])
def create_survey():
    if not Dojo_survey.is_valid(request.form):
        return redirect('/')
    Dojo_survey.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('success.html',survey = Dojo_survey.get_last_survey())
from types import MethodDescriptorType
from flask import Flask,render_template,request,redirect,session
app =  Flask(__name__)
app.secret_key="aaafdsasdf1d9a5f4a6f1d6af1s51d6a"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods= ['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)
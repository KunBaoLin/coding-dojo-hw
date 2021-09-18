from flask import Flask, render_template,request,redirect,session
import random
app = Flask(__name__)
app.secret_key = 'kdsfjsdlahfkoa16789jdsalkfjkafjkafj19859' # set a secret key for security purposes

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    elif 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/guess',methods = ['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)


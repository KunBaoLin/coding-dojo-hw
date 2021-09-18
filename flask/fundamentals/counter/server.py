from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = 'kdsfjsdlahfkoajdsalkfjkafjkafj19859' # set a secret key for security purposes

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/add2')
def add2():
    session['count'] += 2
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)


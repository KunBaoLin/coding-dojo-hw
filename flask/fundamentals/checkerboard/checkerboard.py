from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkerboard.html',row=8, col=8, color1 ='red',color2='black')

@app.route('/<int:x>')
def row(x):
    return render_template('checkerboard.html',row=x, col=8, color1 ='red',color2='black')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template('checkerboard.html',row=x, col=y, color1 ='red',color2='black')

@app.route('/<int:x>/<int:y>/<string:color_one>')
def row_col_color_one(x,y,color_one):
    return render_template('checkerboard.html',row=x, col=y, color1 =color_one,color2='black')

@app.route('/<int:x>/<int:y>/<string:color_one>/<string:color_two>')
def row_col_color_two(x,y,color_one,color_two):
    return render_template('checkerboard.html',row=x, col=y, color1 =color_one,color2=color_two)

if __name__=="__main__":
    app.run(debug=True)
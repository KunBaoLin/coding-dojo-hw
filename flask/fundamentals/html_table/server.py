from flask import Flask, render_template
app = Flask(__name__)

@app.route('/lists')
def render_list():
    users_list = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    for i in range(0,len(users_list)):
        x = ''
        for val in users_list[i].items():
            x += f' {val[1]}'
        users_list[i]['full_name'] = x
    return render_template('table.html',users=users_list)

if __name__=="__main__":
    app.run(debug=True)
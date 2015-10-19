from flask import Flask
#from flask import request # request is global
from flask import render_template

app = Flask(__name__)
# to make app instance, use whatever our current namespace is
# if we call simple_app.py, then the namespace is dunder main, which means it's being run directly
# if we import this file from somewhere, then our namespace will be simple_app
# it means always refer to yourself!


# decorator
# a decorator is a function that wraps around another function and let you do
# things the function
# take this index function
# and register with our app as the route, forward slash
@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    #name = request.args.get('name',name)
    return "Hello from {}".format(name)

# creating routes for your views is a major part of working with basic Flask,
# 4 routes in one view
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    # flask can automatically browse 'templates' folder (and it use Jinja2 engine)
    context = {'num1':num1, 'num2':num2}
    #return render_template('add.html', num1=num1, num2=num2)
    return render_template('add.html', **context)

    #return """
    #<!doctype html>
    #<html>
    #</head>
    #<title>Adding!</title>
    #<body>
    #<h1>{} + {} + {}</h1>
    #</body>
    #</html>
#""".format(num1, num2, num1+num2)
    #return '{} + {} = {}'.format(num1, num2, num1+num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1=5,num2=5):
    return '{}'.format(num1*num2)

# """ triple quotes lets us hold on to line breaks

app.run(debug=True,port=8000)

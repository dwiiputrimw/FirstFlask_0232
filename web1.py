from flask import Flask
#from markusafe import escape
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!"
@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    post_id =post_id+7
    return f"Post {post_id}"



@app.route("/")
def index():
    return "Welcome to TI Student Page!"

@app.route("/hi/<name>")
def hi(name):
    return f"Hello, {name}! Welcome to Informatics."

@app.route("/double/<int:n>")
def double(n):
    return f"Double of {n} is {n * 2}"

@app.route("/age/<int:age>")
def age(age):
    return f"You are {age} years old."

@app.route("/student/<name>/<int:semester>")
def student(name, semester):
    return f"{name} is an Informatics student in semester {semester}."

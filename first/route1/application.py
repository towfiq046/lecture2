from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return "Hello, world!!!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug = True)

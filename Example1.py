from flask import Flask
app = Flask(__name__)
#add a line
@app.route("/")
@app.route("/start")

def start():
    return "Sysops Start Page"

@app.route("/integer/<int:a>")
def int_type(a):
    print(a + 1)
    return "correct"


@app.route('/dynamic/<dq>')
def dynamic(dq):
    return "Dynamic Sysops Test"

@app.route("/float/<float:float_value>")
def float_type(float_value):
    print(float_value + 1)
    return "correct"
# dynamic route that accepts slashes
@app.route("/path/<path:path_value>")
def path_type(path_value):
    print(path_value)
    return "correct"


@app.route('/tool/<name>')
def selection(name):
    if name.lower()=='vidoes':
        return 'Video selection screen holder',200
    else:
        return 'Not found',404

if __name__ == '__main__':
    app.run()
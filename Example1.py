from flask import Flask
app = Flask(__name__)
#add a line
@app.route("/")
@app.route("/start")
def start():
    return "Sysops Start"
@app.route('/dynamic/<dq>')

def dynamic(dq):
    return "Dynamic Sysops Test"

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"
@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"
# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

if __name__ == '__main__':
    app.run()
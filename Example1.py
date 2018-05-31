from flask import Flask
app = Flask(__name__)
#add a line
@app.route("/")
@app.route("/start")
def start():
    return "Sysops Start"

if __name__ == '__main__':
    app.run()


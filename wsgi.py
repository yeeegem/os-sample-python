from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Настя какася!"

if __name__ == "__main__":
    application.run()

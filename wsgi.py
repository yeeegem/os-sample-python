from flask import Flask, request, send_from_directory
application = Flask(__name__, static_url_path='')

@application.route("/")
def hello():
    return application.send_static_file('index.html')

if __name__ == "__main__":
    application.run(debug=True)

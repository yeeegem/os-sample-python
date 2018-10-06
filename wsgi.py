from flask import Flask, request, send_from_directory, render_template
application = Flask(__name__, static_url_path='')

@application.route("/")
def hello():
    ##return application.send_static_file('index.html')
    return render_template('index.html', flask_debug=application.debug)

if __name__ == "__main__":
    application.run(debug=True)

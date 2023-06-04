from flask import Flask, redirect, url_for, request, render_template

application = Flask(__name__)


@application.route('/')
def hello_world():  # put application's code here
    # remove that master code and adding testing code

    return render_template('home.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80)

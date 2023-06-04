from flask import Flask, redirect, url_for, request, render_template

application = Flask(__name__)


@application.route('/')
def hello_world():
    # remove that master code and adding testing code

    return render_template('home.html')

def process():
    # working on image processing
    return "Hello World"
def testing():
    # working on testing function
    return "testing"

def testing2():
    # working on testing function
    return "testing"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80)

from flask import Flask

appen = Flask('__name__')

@appen.route('/asd')
def index():
    return 'Hello world!'
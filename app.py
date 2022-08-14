from flask import Flask

app = Flask('__name__')

@app.route('/asd')
def index():
    return 'Hello world!'
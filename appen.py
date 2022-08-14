from asyncore import read
from flask import Flask

app = Flask('__name__')

@app.route('/')
def index():
    return 'Små brune bisker er de beste biskene'

if __name__ == "__main__":
    app.run()
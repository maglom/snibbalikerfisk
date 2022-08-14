from flask import Flask

appen = Flask('__name__')

@appen.route('/')
def index():
    return 'Hello world!'

if __name__ == "__main__":
    appen.run()
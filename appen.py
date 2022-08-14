from asyncore import read
from flask import Flask

app = Flask('__name__')

with open('ETL/API/VG.html', 'r') as file:
    html = read(file)

@app.route('/')
def index():
    return html

if __name__ == "__main__":
    app.run()
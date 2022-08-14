from asyncore import read
from flask import Flask

app = Flask('__name__')

html = '''
<!DOCTYPE html>
<html>
<head>
<title>Små brune bisker er de beste biskene</title>
</head>
<body>

<h1>Dette er ubestridt</h1>
<p>Ifølge folk.</p>

</body>
</html>'''

@app.route('/')
def index():
    return html

if __name__ == "__main__":
    app.run()
from flask import Flask
import psycopg2

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

@app.route('/person/<query>')
def search(query):
    conn = psycopg2.connect("dbname=d31saoq36iural user=zfyjfnpddtxnrf password=b85ff3d4b5f275531eab6fc8a9c13bff39b7b28f0f05334a7a30e11d0aefa91b", port=5432)
    cur = conn.cursor()
    cur.execute('''select * from person where name = '{query}''')
    return cur.fetchall()

if __name__ == "__main__":
    app.run()
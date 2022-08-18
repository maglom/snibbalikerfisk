
import psycopg2
import psycopg2.extras
from flask import Flask

app = Flask('__name__')


db = 'd26q679v0a08m9'
username = 'wjrnshvsyrjebr'
porti = 5432
pas = 'aa60041333af7760248ef2f67014c80476c9cfd709de727ddb82f680d7d1fc1d'
hosted = 'ec2-52-210-97-223.eu-west-1.compute.amazonaws.com'


@app.route('/')
def index():
    return '''For searching by flight number go here <a href="https://snibbalikerfisk.herokuapp.com/flight_number">/flight_number</a><br>
    For searching by departure and arrival airportcodes go here <a href="https://snibbalikerfisk.herokuapp.com/airport_codes">/airport_codes</a><br>
    For getting all flights departing today go here <a href="https://snibbalikerfisk.herokuapp.com/flights_today">/flights_today</a>
    '''

@app.route('/flight_number')
def flight_number_root():
    return '''Input /flight_number/#flight_number# to search for flightnumber
    Example /flight_number/DY606'''

@app.route('/airport_codes')
def airport_codes_root():
    return '''Input /airport_codes/#airport_codes# to search for flightnumber
    Example /airport_codes/OSL-BGO'''

@app.route('/flight_number/<flight_number>')
def flight_number(flight_number):
    return get_data_flight_number(flight_number)

@app.route('/airport_codes/<airport_codes>')
def airport_codes(airport_codes):
    codes = airport_codes.split('-')
    return get_data_dep_arr(codes[0], codes[1])

@app.route('/flights_today')
def flights_today():
    return get_data_for_todays_flights()

def get_data_flight_number(flight):
    conn = psycopg2.connect(dbname=db, user=username, password=pas, host=hosted)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(f'''
    select * from flight f
    left join distance_flight df on f.id = df.flight_id 
    left join distance d on df.distance_id = d.id 
    left join emission e on d.id = e.distance_id
    where f.flight_code = '{flight}' 
    ''')
    ls = []
    for i in cur:
        ls.append(dict(i))
    conn.close()
    return ls

def get_data_dep_arr(dep, arr):
    conn = psycopg2.connect(dbname=db, user=username, password=pas, host=hosted)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(f'''
    select * from flight f
    left join distance_flight df on f.id = df.flight_id 
    left join distance d on df.distance_id = d.id 
    left join emission e on d.id = e.distance_id
    where d.departure_airport_id = '{dep}' and d.arrival_airport_id = '{arr}' 
    ''')
    ls = []
    for i in cur:
        ls.append(dict(i))
    conn.close()
    return ls

def get_data_for_todays_flights():
    conn = psycopg2.connect(dbname=db, user=username, password=pas, host=hosted)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(f'''
    select * from flight f
    left join distance_flight df on f.id = df.flight_id 
    left join distance d on df.distance_id = d.id 
    left join emission e on d.id = e.distance_id
    where date(f.time_departure) = current_date
    ''')
    ls = []
    for i in cur:
        ls.append(dict(i))
    conn.close()
    return ls

if __name__=='__main__':
    app.run(debug=True)




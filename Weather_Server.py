import pyowm

from bottle import route, run, template


@route('/weather/<name>')
def index(name):
    city = str(name) # Home City
    owm = pyowm.OWM('be57dbc6baf1834cfa057f6b9e3af075') # My Open Weather API Key
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    temp = temperature.get('temp')
    tomorrow = pyowm.timeutils.tomorrow()
    wind = w.get_wind()
    wind_speed = wind["speed"]
    return template(
        '<b>The temperature in {{city}} is {{temp}} celsius with a {{wind_speed}} m/s wind speed</b>!'
        '<p><p>But where else would you like to be tomorrow? Somewhere '
        '<a href="http://localhost:8080/seek/hot">Hot</a>, '
        '<a href="http://localhost:8080/seek/cold">Cold</a> '
        'or <a href="http://localhost:8080/seek/temperate">Temperate</a>?<p><p>', city=city, temp=temp, temperature=temperature, wind_speed=wind_speed
    )

@route('/seek/hot')
def index():
    return "Ah so you like it Hot do you?" # Temporary holding text


@route('/seek/cold')
def index():
    return "Ah so you like it Cold do you?" # Temporary holding text

@route('/seek/temperate')
def index():
    return "Ah so you like it Temperate do you?" # Temporary holding text

run(host='localhost', port=8080)

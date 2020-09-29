from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/',)
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def results():
	city = request.form["city"].title()
	url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=d303629e689b7b8a3ac63f069ee6d766"
	response = requests.get(url.format(city)).json()
	if response["cod"] == "400" or response["cod"] == "404":
		return render_template('index.html')
	weather = {
	"city" : city,
	"country" : response["sys"]["country"],
	"temperature" : int(response["main"]["temp"]),
	"description" : response["weather"][0]["description"].capitalize(),
	"icon": response["weather"][0]["icon"]
	}
	icon_url = "http://openweathermap.org/img/wn/{}@2x.png".format(weather["icon"])
	return render_template('index.html', city = city, country = weather["country"], temperature = str(weather["temperature"]) + " °C",
	 description = weather["description"], icon_url = icon_url)
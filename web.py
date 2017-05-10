from flask import Flask, render_template, request
import google_api
app = Flask(__name__)

####################################This is using the Google Places API#############################################

@app.route("/")
def index():
	address = request.values.get('address') #
	food = None 						# initially set it to none
	if address:                             # weather look-up happens only if 'address' variable is set
		food = google_api.search_food(address) #
	return render_template('index.html', food=food) #

# #################################This is using the Weather API#############################################

# @app.route("/")
# def index():
# 	address = request.values.get('address') #
# 	forecast = None 						# initially set it to none
# 	if address:                             # weather look-up happens only if 'address' variable is set
# 		forecast = weather.get_weather(address) #
# 	return render_template('index.html', forecast=forecast) #

##################################################################################
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/thanks')
def thanks():
	return render_template('thanks.html')

if __name__ == "__main__":
	app.run()
from flask import Flask, render_template, request
import google_api
import os
app = Flask(__name__)

####################################This is using the Google Places API#############################################

@app.route("/")
def index():
	address = request.values.get('address') #
	food = None 						# initially set it to none
	if address:                             # weather look-up happens only if 'address' variable is set
		food = google_api.search_food(address) #
	return render_template('index.html', food=food) #


##################################################################################
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/thanks')
def thanks():
	return render_template('thanks.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
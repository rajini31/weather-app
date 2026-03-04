from flask import Flask, render_template, request
import urllib.request
import json

app = Flask(__name__)

API_KEY = "api key"   # Put your API key here

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())

            if data["cod"] == 200:
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "icon": data["weather"][0]["icon"]
                }
            else:
                error = "City Not Found"

        except:
            error = "Something went wrong"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)

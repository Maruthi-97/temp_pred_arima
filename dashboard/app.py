from flask import Flask, render_template
import folium

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/map")
def map():
    start_coords = (42.9974521, -78.7907883)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()


if __name__ == '__main__':
	app.run(debug=True)
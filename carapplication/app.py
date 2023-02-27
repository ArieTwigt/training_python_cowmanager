from flask import Flask, render_template, request
from custom_modules.cardata import CarData


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/random_cars_brand', methods=['GET', 'POST'])
def random_cars_brand():
    if request.method == "POST":
        selected_brand = request.form.get("brand")
        car_data = CarData(selected_brand, "WIT")
        car_data.import_cars_brand()
        car_data.select_columns("kenteken", "merk", "handelsbenaming", "catalogusprijs")
        cars = car_data.get_data() # pandas data frame
        cars_list = cars.to_dict("records") # converteer pandas naar list/dict structuur
        return render_template("random_cars_brand.html", cars=cars_list)
    else:
        return render_template("random_cars_brand.html")

if __name__ == "__main__":
    app.run()
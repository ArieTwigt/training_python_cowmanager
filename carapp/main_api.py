from custom_modules.import_functions import import_cars, import_car_license
from custom_modules.export_functions import export_df, export_car_plate


if __name__ == "__main__":
    selected_plate = input("Insert the number plate:\n") or "rd-799-k"

    selected_car = import_car_license(selected_plate)
    export_car_plate(selected_car, selected_plate)
    pass
    #selected_brand = input("Select brand (TOYOTA): \n") or "TOYOTA"
    #data = import_cars(selected_brand)
    #export_df(data, selected_brand)
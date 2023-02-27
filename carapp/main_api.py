from custom_modules.cardata import CarData, CarDataCollection


if __name__ == '__main__':
    car_data = CarData("BMW", "WIT")
    car_data.import_cars_brand()
    car_data.select_columns("merk", "handelsbenaming", "catalogusprijs", "eerste_kleur")
    car_data.remove_empty_rows("catalogusprijs")
    car_data.remove_empty_rows("eerste_kleur")
    car_data.modify_data_types(catalogusprijs=float, eerste_kleur=str)
    car_data.remove_outliers("catalogusprijs")
    car_data.data_summary()


    car_data_2 = CarData("AUDI", "WIT")
    car_data_2.import_cars_brand()
    car_data_2.select_columns("merk", "handelsbenaming", "catalogusprijs", "eerste_kleur")
    car_data_2.remove_empty_rows("catalogusprijs")
    car_data_2.modify_data_types(catalogusprijs=float, eerste_kleur=str)
    car_data_2.remove_outliers("catalogusprijs")
    car_data_2.data_summary()

    # initiate Car data collection
    car_data_collection = CarDataCollection("My collection")
    car_data_collection.add_car_data(car_data)
    car_data_collection.add_car_data(car_data_2)

    pass

    # export the data
    #car_data.export_cars_brand()




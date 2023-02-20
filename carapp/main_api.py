from custom_modules.import_functions import import_cars

selected_brand = input("Select brand (TOYOTA): \n") or "TOYOTA"

data = import_cars(selected_brand)

print(data.head())

pass
import requests
import sys
import pandas as pd



def import_cars(brand):
    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # validate if the request went succesfull
    if response.status_code != 200:
        print("Error")
        sys.exit()


    # get the data
    cars_list = response.json()

    # convert to a pandas DataFrame
    cars_df = pd.DataFrame(cars_list)

    # return the data frame
    return cars_df
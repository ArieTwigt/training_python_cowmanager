import requests
import sys
import pandas as pd


RDW_ENDPOINT = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"


def import_cars_brand(brand: str, color:str) -> pd.DataFrame:
    '''
    Function that imports car data from the RDW

    Params:
    * brand (str)
    
    '''


    # uppercase the brand
    brand_upper = brand.upper()
    color_upper = color.upper()

    # define the endpoint
    endpoint = f"{RDW_ENDPOINT}?merk={brand_upper}&eerste_kleur={color_upper}"

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


def import_car_plate(plate: str) -> pd.DataFrame:
    '''
    Imports a car based on the license plate

    Params:
    * plate (str): The license plate of the car
    '''
    if type(plate) != str:
        raise TypeError(f"Brand moet een 'str' zijn. Nu is het een {type(plate)}")

    # uppercase the license plate
    plate_upper_clean = plate.upper().replace("-", "")


    # compose the endpoint for the API request
    endpoint = f"{RDW_ENDPOINT}?kenteken={plate_upper_clean}"

    # execute the request
    response = requests.get(endpoint)

    # check if the response went succesfully
    if response.status_code != 200:
        print("Something went wrong")
        sys.exit()

    # extract the data
    selected_car = response.json()

    # convert to a DataFrame
    car_df = pd.DataFrame(selected_car)

    return car_df


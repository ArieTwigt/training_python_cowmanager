import pandas as pd
import os


def export_cars_brand(df: pd.DataFrame, brand: str="Unknown") -> None:
    
    # list files and folders
    folders = os.listdir("carapp/export")

    if brand not in folders:
        print(f"Folder {brand} does not exist. Creating 📂")
        os.mkdir(f"carapp/export/{brand}")

    # file name
    file_name = f"export_{brand}.csv"

    # create the sub-folder
    export_path = f"carapp/export/{brand}/{file_name}"

    # export the file
    df.to_csv(export_path, 
              index=False,
              sep=";")

    print(f"✅ Succesfully exported to path {export_path}")


def export_car_plate(df: pd.DataFrame, plate: str="Unkown") -> None:
    '''
    Exports the file
    
    '''

    # make the plate lowercase
    plate_lower = plate.lower()

    # specify the folder path
    folder_path = f"carapp/export/plates/{plate_lower}"

    # create the folder
    os.mkdir(folder_path)

    # create the file path
    file_path = f"{folder_path}/export_{plate_lower}.csv"

    # export the file
    df.to_csv(file_path,
              index=False, 
              sep=";")


    
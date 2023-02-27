import pandas as pd
import os





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


    
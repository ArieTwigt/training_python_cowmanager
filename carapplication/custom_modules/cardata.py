import requests
import sys
import pandas as pd
import os

class CarDataCollection:
    
    _car_data_list = []

    def __init__(self, name):
        self.name = name


    def add_car_data(self, CarData):
        self._car_data_list.append(CarData)
    

    def show_car_data_list(self):
        for car_data in self._car_data_list:
            print(car_data.data_summary())


class CarData:
    
    rdw_endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    steps = []
    status = "New"
    _data = None
    

    def __init__(self,  brand: str, color: str=None):
        '''
        Initializes the CarData object with the given brand and optional color.
    
        Args:
        - brand (str): The brand of the car.
        - color (str, optional): The color of the car. Defaults to None.
        '''
        
        # verify the right types
        if type(brand) != str and brand != None:
            raise TypeError(f"Parameter 'brand' must be of type 'str'\nGot {type(brand)}")

        if type(color) != str and color != None:
            raise TypeError(f"Parameter 'color' must be of type 'str'\nGot {type(color)}") 

        self.brand = brand
        self.color = color
        self.steps.append("Initialized")


    def import_cars_brand(self) -> pd.DataFrame:
        '''
        Imports car data from the RDW API and stores it in a pandas DataFrame.
    
        Returns:
        - pd.DataFrame: The imported car data as a pandas DataFrame.
    
        Raises:
        - SystemExit: If the API request returns a non-200 status code.
        '''


        # uppercase the brand
        brand_upper = self.brand.upper()

        if self.color == None:
            # define the endpoint
            endpoint = f"{self.rdw_endpoint}?merk={brand_upper}"
        else:
            color_upper = self.color.upper()
            endpoint = f"{self.rdw_endpoint}?merk={brand_upper}&eerste_kleur={color_upper}"

        # execute the request
        response = requests.get(endpoint)

        # validate if the request went succesfull
        if response.status_code != 200:
            print("Error")
            sys.exit()


        # get the data
        cars_list = response.json()

        # check if the list is empty
        if len(cars_list) == 0:
            raise ValueError(f"No data could be imported for {brand_upper} and {color_upper}")
        
        # convert to a pandas DataFrame
        cars_df = pd.DataFrame(cars_list)

        # change the status
        self.status = "Data imported"

        # add the step
        self.steps.append("Data imported")

        # return the data frame
        self._data = cars_df

    
    def select_columns(self, *args: str):
        '''
        Filters the CarData object to only include the selected columns.
    
        Args:
        - *args: A variable number of arguments, each representing a column to include in the filtered DataFrame.
        '''
        selected_columns = list(args)

        df_columns_list = list(self._data.columns)

        # Check if the column is available
        for column in selected_columns:
            if column not in df_columns_list:
                raise ValueError(f"The column {column} does not exist in the DataFrame")


        # only maintain the selected columns
        data_selected = self._data[selected_columns]
        
        self._data = data_selected
        
        # change the status
        self.status = "Filtered columns"

        # add to the steps
        self.steps.append("Filtered columns")
    

    def remove_empty_rows(self, selected_column):
        '''
        Removes rows from the CarData object that have missing values in the specified column.
    
        Args:
        - selected_column (str): The name of the column to check for missing values.
        '''

        data_selected = self._data[self._data[selected_column].notna()]
        
        self._data = data_selected

        # change the status
        self.status = f"Remove empty columns for {selected_column}"

        # add to the steps
        self.steps.append(f"Remove empty columns for {selected_column}")

    
    def modify_data_types(self, **kwargs):
        '''
        Modifies the data types of specified columns in the CarData object.
    
        Args:
        - **kwargs: A dictionary containing column names as keys and desired data types as values.
        '''
        data_selected = self._data

        # change the data types of the columns
        for column, data_type in kwargs.items():
            data_selected[column] = data_selected[column].astype(data_type)
        
        # update the data
        self._data = data_selected

        # change the status
        self.status = "Modified data types"

        # add to steps
        self.steps.append("Modified data types")


    def remove_outliers(self, selected_column):
        '''
        Removes rows from the CarData object that have values in the specified column outside of two standard deviations from the mean.
    
        Args:
        -
        '''
        data_selected = self._data


        mean_value = data_selected[selected_column].mean()
        std_dev = data_selected[selected_column].std()
        min_border = mean_value - (std_dev * 2)
        max_border = mean_value + (std_dev * 2)

        data_filtered = data_selected.query(f"{selected_column} > @min_border & {selected_column} < @max_border")
        
        # update the data
        self._data = data_filtered

        # update the status
        self.status = "Removed outliers"

        # update the steps
        self.steps.append("Removed outliers")


    
    def data_summary(self):
        '''
        Sumamry of the data
        '''
        data_selected = self._data

        # summarize the steps
        steps_summary = " * " +"\n * ".join(self.steps)

        # show number of rows
        rows_summary = len(data_selected)

        # show the first 5 rows
        preview_summary = data_selected.head()

        # compose the summary
        print(f"Status: {self.status}")
        print("="*10)
        print(steps_summary)
        print("-"*10)
        print(rows_summary)
        print("-"*10)
        print(preview_summary)
        print("-"*10)


    def get_data(self):
        return self._data


    def export_cars_brand(self) -> None:
    
        # list files and folders
        folders = os.listdir("carapp/export")

        if self.brand not in folders:
            print(f"Folder {self.brand} does not exist. Creating 📂")
            os.mkdir(f"carapp/export/{self.brand}")

        # file name
        file_name = f"export_{self.brand}.csv"

        # create the sub-folder
        export_path = f"carapp/export/{self.brand}/{file_name}"

        # export the file
        df = self._data

        df.to_csv(export_path, 
                    index=False,
                    sep=";")

        print(f"✅ Succesfully exported to path {export_path}")


    def __repr__(self) -> str:
        return f"Data for: {self.brand}-{self.color}.\nStatus: {self.status}\nSteps: {self.steps}"
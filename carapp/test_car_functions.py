import pytest
from custom_modules.cardata import CarData, CarDataCollection


CARDATA = CarData("TOYOTA", "GRIJS")
CARDATA.import_cars_brand()

# tests for data types
def test_cardata_inputs_right():
    cardata = CarData("OPEL", "WIT")
    assert cardata.status == 'New'
    
    cardata_2 = CarData("AUDI", "ROOD")
    assert cardata_2.status == 'New'


def test_cardata_inputs_wrong():
    
    with pytest.raises(TypeError):
        CarData("AUDI", 30)
        CarData(100.0, "PUNTO")
        CarData(None, "MICRA")
        CarData("NISSAN")


# tests for data structure
def test_cardata_dataframe_structure():
    
    # check the length of the data frame
    assert len(CARDATA.get_data()) == 1000

    # check the columns of the data frame
    required_columns = ['kenteken', 'voertuigsoort', 'merk', \
                        'handelsbenaming', 'eerste_kleur', 'catalogusprijs']

    current_columns = CARDATA.get_data().columns

    for column in required_columns:
        assert column in current_columns

    
    # check the columns when we specify the columns
    cols_to_select = ['kenteken', 'merk', 'catalogusprijs']
    
    
    CARDATA.select_columns('kenteken', 'merk', 'catalogusprijs')

    assert list(CARDATA.get_data().columns) == cols_to_select

def test_cardata_dataframe_structure_wrong():
    cardata = CarData("Arie", "Arie")

    # make sure the ValueError is raised when there was not data available
    with pytest.raises(ValueError): 
        cardata.import_cars_brand()

    # make sure we do not get the status 'Data imported' if there is no content
    cardata.status != "Data imported"
    

# tests for content

from argparse import ArgumentParser
from custom_modules.import_functions import import_cars_brand, import_car_plate
from custom_modules.export_functions import export_cars_brand, export_car_plate
import sys

# initiate the argument parser
parser = ArgumentParser()

# add arguments to the argument parser
parser.add_argument("--mode", "-m",
                    type=str,
                    required=True,
                    default="brand",
                    choices=["brand", "plate"],
                    help="Decide if you would like to import by plate or by brand.")

parser.add_argument("--brand", "-b", 
                    type=str, 
                    required=False,
                    help="Specify the brand you would like to import.")

parser.add_argument("--color", "-c",
                    type=str,
                    default="WIT",
                    help="Select a color of the cars you would like to import.")

parser.add_argument("--plate", "-p",
                    type=str, 
                    required=False,
                    help="Specify the license plate you would like to import.")

parser.add_argument("--export",
                    type=bool,
                    required=False,
                    default=False,
                    choices=[True, False],
                    help="Indicate if the data should be exported.")


# parse the arguments
args = parser.parse_args()

# run the script
if __name__ == '__main__':
    # get the brand from the argument parser
    mode = args.mode
    selected_color=args.color
    selected_brand = args.brand
    selected_plate = args.plate
    export = args.export

    # check if we import by plate or brand
    if mode == 'brand' and selected_brand == None:
        print("For mode 'brand', specify a brand with --brand")
        sys.exit()
    
    if mode == 'plate' and selected_plate == None:    
        print("For mode 'plate', specify a plate with --plate")
        sys.exit()

    # specify the mode:
    print(f"🚗 Selected for the mode {mode}")

    # apply the import function for brand
    if mode == "brand":
        cars_df = import_cars_brand(selected_brand,
                                    selected_color)

        # decide to export
        if export:
            export_cars_brand(cars_df, selected_brand)

    # apply the import function for plate
    if mode == "plate":
        cars_df = import_car_plate(selected_plate)

        # decide to export
        if export:
            export_car_plate(cars_df, selected_plate)
        

 


 

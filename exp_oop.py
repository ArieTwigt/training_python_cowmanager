class Garage:
    _items = []
    
    def __init__(self, name):
        self.name = name

    def add_item(self, Car):
        self._items.append(Car)

    def show_items(self):
        for item in self._items:
            print(item) 

    def calculate_items_value(self, store_value=False, return_value=True):

        total_value = 0
        for item in self._items:
            total_value += item.price

        if store_value:
            self.total_value = total_value
        
        if return_value:
            return total_value
    


class Vehicle:
    # default parameters
    price = 0
    status = "AVAILABLE"
    voertuig_wielen = 4
    
    
    def reserve_car(self):
        print(f"Old satus was {self.status}")
        self.status = "RESERVED"
        print(f"New status is {self.status}")

    def set_price(self, price: float):
        self.price = price

    def apply_discount(self, discount_rate: float):

        # validations
        discount_limit = 0.3
        if discount_rate > discount_limit:
            raise ValueError(f"💸 Discount rate should be between 0.3 and 0. \nGot '{discount_rate}'")


        print(f"Old price {self.price}")
        self.price *= (1 - discount_rate)
        print(f"New price = {self.price}")

    def __repr__(self) -> str:
        return f"Name: {self.name}"



class Car(Vehicle):

    def __init__(self, brand: str, 
                 model: str) -> None:

        # parameters from initialization
        self.brand = brand
        self.model = model
    

    def __repr__(self) -> str:
        return f"{self.brand} - {self.model} - {self.price} - {self.status}"
        

class Bike(Vehicle):

    voertuig_wielen = 2

    def __init__(self, brand: str, 
                 model: str) -> None:

        # parameters from initialization
        self.brand = brand
        self.model = model


    def __repr__(self) -> str:
        return f"{self.brand} - {self.model} - {self.price} - {self.status}"


if __name__ == '__main__':
    my_garage = Garage("Arie's Garage")

    car_1 = Car("OPEL", "VECTRA")
    car_1.set_price(1000)
    
    car_2 = Car("TOYOTA", "COROLLA")
    car_2.set_price(5000)

    bike_1 = Bike("Kawasaki", "Katana")
    bike_1.set_price(4000)

    bike_2 = Bike("Ducati", "Pizza")
    bike_2.set_price(3000)

    # add the vehicles to the garage
    my_items = [car_1, car_2, bike_1, bike_2]

    for item in my_items:
        my_garage.add_item(item)

    # calculate the total value of the vehicles
    my_garage_total_value = my_garage.calculate_items_value()
    print(my_garage_total_value)
    pass
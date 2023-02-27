# decorator
def correct_inflation(func):
    print("Applied inflation")
    def wrapper(amount, rate, years):
        result = func(amount, rate / 2, years)
        return result
    
    return wrapper


# decorator
def correct_rally(func):
    print("Applied rally")
    def wrapper(amount, rate, years):
        result = func(amount, rate * 2, years)
        return result
    
    return wrapper


def print_interest(func):

    def wrapper(amount, rate, years):
        for year in range(years):
            amount = func(amount, rate, year + 1)
            print(f"{year + 1}: {amount}")
    
    return wrapper


# base function
def calc_interest(amount, rate, years):
    result = amount * (1+rate) **years
    return result

# old way to apply decorator
calc_interest_inflation = correct_inflation(calc_interest)
calc_interest_rally = correct_rally(calc_interest)


@correct_inflation
@print_interest
def calc_interest_inflation_print(amount, rate, years):
    result = amount * (1+rate) **years
    return result



@correct_rally
@print_interest
def calc_interest_rally_print(amount, rate, years):
    result = amount * ( 1+ rate) ** years
    return result



if __name__ == '__main__':
    print("="*15)
    calc_interest_inflation_print(1000, 0.05, 10)
    print("="*15)
    calc_interest_rally_print(1000, 0.05, 10)
    
    pass
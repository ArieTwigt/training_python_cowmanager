import pytest

# define the function
def calc_interest(amount: int, rate: float, years: int) -> float:
    if amount > 5000:
        raise ValueError("Amount is too high")
    
    # check for amount and rate
    available_types_amount_rate = [int, float]

    for param in (amount, rate):
        if type(param) not in available_types_amount_rate:
            raise TypeError(f"Type of {param} is not a required type")
        
    # check for year
    if type(years) != int:
        raise TypeError(f"Year should be of type int\ngot {type(years)}")
    
    result = amount * (1+rate) **years
    return result

# define the test(s)

# test for the calc_interest function
def test_calc_interest():
    assert calc_interest(1000, 0.05, 1) == 1050
    assert calc_interest(1000, 0.10, 1) == 1100


def test_calc_interest_wrong():
    with pytest.raises(ValueError):
        calc_interest(5001, 0.05, 1)
    with pytest.raises(TypeError):
        calc_interest(1000, "arie", 10)
    with pytest.raises(TypeError):
        calc_interest(1000, 0.5, "arie")

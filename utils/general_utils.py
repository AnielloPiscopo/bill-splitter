import random
from collections import defaultdict
from typing import Optional

def get_num_greater_than_x(x:float)->float:
    """
    Reads a numeric value from user input and checks if it is greater than a given threshold.

    Args:
        x (float): The lower bound that the input value must exceed.

    Returns:
        float: The numeric value inserted by the user if valid.

    Raises:
        ValueError: If the input is not greater than x or is not numeric.
    """

    friends_num = float(input().strip())

    if friends_num > x:
        return friends_num
    else:
        raise ValueError()

def get_str_list_with_x_elements(length:int)->list[str]:
    """
    Reads a fixed number of strings from user input and returns them as a list.

    Args:
        length (int): Number of strings to read.

    Returns:
        list[str]: A list containing the inserted strings.
    """

    str_list = []

    for i in range(length):
        str_list.append(input().strip())

    return str_list

def get_rounded_num_by_division(
    dividend: float,
    divisor: int,
    digits_num: int
) -> float:
    """
    Divides two numbers and rounds the result to a specified number of decimal digits.

    Args:
        dividend (float): The number to be divided.
        divisor (int): The number by which the dividend is divided.
        digits_num (int): Number of decimal digits for rounding.

    Returns:
        float: The rounded result of the division.
    """

    return round(dividend / divisor, digits_num)

def get_defaultdict_with_same_value(
    keys: list[str],
    value: float,
    exceptions: Optional[list[str]] = None,
    specific_value: Optional[float] = None
) -> dict[str, float]:
    """
    Creates a dictionary where all keys are assigned the same value,
    except for optional exception keys that receive a specific value.

    Args:
        keys (list[str]): List of keys to be used in the dictionary.
        value (float): Default value assigned to all keys.
        exceptions (Optional[list[str]]): Keys that must receive a different value.
        specific_value (Optional[float]): Value for the exception keys.

    Returns:
        dict[str, float]: The resulting dictionary with assigned values.
    """

    result = {}

    for key in keys:
        result[key] = specific_value if exceptions and key in exceptions else value

    return result

def get_user_boolean_answer()->bool:
    """
    Asks the user a yes/no question and returns the corresponding boolean value.

    Returns:
        bool: True if the user answers 'yes', False if the user answers 'no'.
    """

    while True:
        print("Insert your choice.Yes or No?")
        user_choice = input().strip().lower()

        match user_choice:
            case "yes":
                return True
            case "no":
                return False
            case _:
                print("Not a valid choice")

def get_rnd_el(elements:list[str])->str:
    """
    Selects and returns a random element from a list.

    Args:
        elements (list[str]): List of elements.

    Returns:
        str: A randomly selected element from the list.
    """

    return random.choice(elements)
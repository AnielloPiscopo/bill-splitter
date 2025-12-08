import random
from collections import defaultdict
from typing import Optional

def get_num_greater_than_x(x:float)->float:
    friends_num = float(input().strip())

    if friends_num > x:
        return friends_num
    else:
        raise ValueError()

def get_str_list_with_x_elements(length:int)->list[str]:
    str_list = []

    for i in range(length):
        str_list.append(input().strip())

    return str_list

def get_rounded_num_by_division(
    dividend: float,
    divisor: int,
    digits_num: int
) -> float:
    return round(dividend / divisor, digits_num)

def get_defaultdict_with_same_value(
    keys: list[str],
    value: float,
    exceptions: Optional[list[str]] = None,
    specific_value: Optional[float] = None
) -> dict[str, float]:

    result = {}

    for key in keys:
        result[key] = specific_value if exceptions and key in exceptions else value

    return result



def get_user_boolean_answer()->bool:
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
    return random.choice(elements)
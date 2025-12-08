from utils.general_utils import get_rnd_el , get_num_greater_than_x , get_str_list_with_x_elements , get_defaultdict_with_same_value ,get_rounded_num_by_division , get_user_boolean_answer
from typing import Optional


# write your code here
def start_billsplitter()->None:
    """
    Starts the Bill Splitter application flow.

    Handles user input, bill calculation, lucky participant selection,
    and prints the final result.
    """
    try:
        friends_num:int = get_friends_num()
        friends_list:list[str] = get_friends_list(friends_num)
        bill:float = get_bill()
        lucky_one:Optional[str]=get_the_lucky_one(friends_list)
        splitted_bill = get_splitted_bill(bill , friends_num , lucky_one)

        friends_dict:dict[str , float] =  get_friends_dict_with_bills(friends_list , splitted_bill , lucky_one)
        print(friends_dict)
    except ValueError as e:
        print(e)

def get_friends_num()->int:
    """
    Asks the user to insert the number of friends joining the party.
    """
    print("INSERT THE NUM OF FRIENDS")

    try:
        return int(get_num_greater_than_x(0))
    except ValueError:
        raise ValueError("No one is joining for the party")

def get_bill()->float:
    """
    Asks the user to insert the total bill amount.
    """
    print("INSERT THE TOTAL BILL")

    try:
        return get_num_greater_than_x(0)
    except ValueError:
        raise ValueError("The bill value is invalid")

def get_splitted_bill(
    total_bill: float,
    guests_num: int,
    lucky_one: Optional[str] = None
) -> float:
    """
    Calculates the individual bill share based on the number of guests
    and the presence of a lucky participant.
    """
    if lucky_one is not None and guests_num == 1:
        raise ValueError("Cannot split the bill with only one guest and a lucky one")

    real_guests = guests_num - 1 if lucky_one else guests_num
    return get_rounded_num_by_division(total_bill, real_guests, 2)


def get_friends_list(friends_num:int)->list[str]:
    """
    Collects the list of friends' names from user input.
    """
    print("INSERT THE FRIENDS' NAMES")
    return get_str_list_with_x_elements(friends_num)

def get_friends_dict_with_bills(
    friends_list: list[str],
    splitted_bill: float,
    lucky_one: Optional[str] = None
) -> dict[str, float]:
    """
    Creates a dictionary that associates each friend with their split bill amount.
    """

    exceptions: Optional[list[str]] = [lucky_one] if lucky_one else None

    return get_defaultdict_with_same_value(
        friends_list,
        splitted_bill,
        exceptions,
        0
    )


def get_the_lucky_one(friends_list:list[str])->Optional[str]:
    """
    Determines whether a lucky participant will be selected and returns their name.
    """

    print("Do you want to have a lucky one?")

    if get_user_boolean_answer() :
        lucky_one:str = get_rnd_el(friends_list)
        print(lucky_one , "is going to be lucky")
        return lucky_one
    else:
        print("No one is going to be lucky")
        return None
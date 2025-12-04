from utils.general_utils import get_rnd_el , get_num_greater_than_x , get_str_list_with_x_elements , get_defaultdict_with_same_value ,get_rounded_num_by_division , get_user_boolean_answer
from typing import Optional


# write your code here
def get_friends_num()->int:
    try:
        print("INSERT THE NUM OF FRIENDS")
        return int(get_num_greater_than_x(0))
    except ValueError:
        raise ValueError("No one is joining for the party")

def get_bill()->float:
    try:
        print("INSERT THE TOTAL BILL")
        return get_num_greater_than_x(0)
    except ValueError:
        raise ValueError("The bill value is invalid")

def get_splitted_bill(total_bill:float , guests_num:int , lucky_one:Optional[str]=None)->float:
    return (get_rounded_num_by_division(total_bill , guests_num , 2) if lucky_one is None
            else get_rounded_num_by_division(total_bill , guests_num-1 , 2))

def get_friends_list(friends_num)->list[str]:
    print("INSERT THE FRIENDS' NAMES")
    return get_str_list_with_x_elements(friends_num)

def get_friends_dict_with_bills(friends_list:list[str] , splitted_bill:float , lucky_one:Optional[str]=None)->dict[str , float]:
    exceptions:Optional[str] = [lucky_one] if lucky_one is not None else None

    return dict(get_defaultdict_with_same_value(friends_list, splitted_bill , exceptions , 0))

def get_the_lucky_one(friends_list:list[str])->Optional[str]:
    print("Do you want to have a lucky one?")

    if get_user_boolean_answer() :
        lucky_one:str = get_rnd_el(friends_list)
        print(lucky_one , "is going to be lucky")
        return lucky_one
    else:
        print("No one is going to be lucky")
        return None
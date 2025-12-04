from billsplitter import (get_friends_num , get_friends_list , get_bill , get_the_lucky_one , get_splitted_bill , get_friends_dict_with_bills)
from typing import Optional

def main()->None:
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



if __name__ == '__main__':
    main()
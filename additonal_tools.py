import globals

# To print long lists in comfortable way, should be > 5
MAX_PRINT_LIST_NUMBER = 10

# Need to point on something
LIST_POINT_TO = {
    "personal": "You have ",
    "uncertain": "There are ",
    "empty": "",
}


# Usage:
# Just put any dict or list inside and get string outside
def tool_list_to_string(some_list, appeal=None, shorten_list=True):
    if appeal not in LIST_POINT_TO:
        appeal = LIST_POINT_TO["uncertain"]
    else:
        appeal = LIST_POINT_TO[appeal]
    if type(some_list) is dict:
        if "name" in some_list:
            list_name = some_list["name"]
        else:
            list_name = "thing"
        if len(some_list["contain"]) == 0:
            output_string = appeal + "no any " + list_name + "s"
        elif len(some_list["contain"]) == 1:
            output_string = appeal + "one " + list_name + ", it is the " + str(some_list["contain"][0])
        elif len(some_list["contain"]) > MAX_PRINT_LIST_NUMBER and shorten_list:
            output_string = appeal + ', '.join(map(str, some_list["contain"][:4])) + " and " + \
                            str(len(some_list["contain"]) - 4) + " more " + list_name + "s"
        else:
            output_string = appeal + str(len(some_list["contain"])) + " " + list_name + "s, it is: " + \
                            ', '.join(map(str, some_list["contain"][:len(some_list["contain"]) - 1])) + " and " + \
                            str(some_list["contain"][-1])
    elif type(some_list) is list:
        if len(some_list) == 0:
            output_string = appeal + "no anything like this"
        elif len(some_list) == 1:
            output_string = appeal + "only " + str(some_list[0])
        elif len(some_list) > MAX_PRINT_LIST_NUMBER and shorten_list:
            output_string = appeal + ', '.join(map(str, some_list[:4])) + " and " + str(len(some_list) - 4) + \
                  " more of this"
        else:
            output_string = appeal + ', '.join(map(str, some_list[:len(some_list) - 1])) + " and " + str(some_list[-1])
    else:
        raise TypeError("This function is for list or dict only! " + str(type(some_list)) + " incoming!")
    return output_string

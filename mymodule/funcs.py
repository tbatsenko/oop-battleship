# file: funcs.py


def get_valid_input(input_str, valid_options):
    """
    (str), (str) -> (str)
    This function gets data from user
    :param input_str: a msg that will be displayed to user when asking for data
    :param valid_options: all valid options of data
    :return: (str) - user's option
    """
    input_str += " ({}) ".format(", ".join(valid_options))
    resp = input(input_str)
    while resp.lower() not in valid_options:
        resp = input(input_str)
    return resp

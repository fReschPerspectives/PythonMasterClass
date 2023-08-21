import Dictionaries

def my_deep_copy(d: dict = Dictionaries.get_names_dict()) -> dict:
    """
    :param d: dictionary to copy
    :return: a dictionary that is a copy of the original
    """
    copied_dict = {}

    for key, value in d.items():
        copied_dict[key] = copied_dict.setdefault(key, value)

    return copied_dict

copied_names_dict = my_deep_copy()
print(copied_names_dict)

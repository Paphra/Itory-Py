def rows(list_: list, key_: str):
    """
    This function sorts the given list basing on the key
    :param list_: list
    :param key_: str
    :return: list of the sorted rows
    """
    _key_value_list = []
    for _line in list_:
        _key_value_list.append(_line[key_])
    _key_value_list.sort(reverse=True)

    _sorted_list = []
    for _key_value in _key_value_list:
        for _line in list_:
            if _key_value == _line[key_] and _line not in _sorted_list:
                _sorted_list.append(_line)

    list_[:] = _sorted_list[:]

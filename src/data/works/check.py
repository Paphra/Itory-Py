
def if_empty(_list: list, _return: dict):
    """
    Checking to see if the given list is empty
    If it is empty, then an item us added indicating that nothing is found
    in the list
    :param _list: list of the items or rows to be checked
    :param _return: the return item or row if the list is empty
    :return: list containing either the empty row or the original list
    if it found not to be empty
    """
    list_ = _list
    if not list_:
        list_ = [_return]
    return list_


def check_rows(rows_list: list, titles: list, _keys_: list):
    """
    Checking the rows to see if they are okay
    :return:
    """
    if len(rows_list) == 0:
        no_rows = {}
        for _t in titles:
            if titles.index(_t) == 0:
                no_rows[_keys_[0]] = 'Nothing is Found!'
            else:
                no_rows[_keys_[titles.index(_t)]] = ''
        return [no_rows]
    return rows_list

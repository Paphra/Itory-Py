
def if_empty(_list: list, _return: dict):
    list_ = _list
    if len(list_) == 0:
        list_ = [_return]
    return list_

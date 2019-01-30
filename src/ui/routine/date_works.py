

def split_date(_date_line):
    _datetime = _date_line.split('|')
    _date = _datetime[0]
    _dt = _date.split('-')
    _time = _datetime[1]
    _t = _time.split(':')
    return {'year': _dt[0],
            'month': _dt[1],
            'day': _dt[2],
            'hour': _t[0],
            'minute': _t[1],
            'second': _t[2]}

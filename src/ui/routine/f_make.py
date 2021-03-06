from datetime import datetime


def focus(inst_):
    inst_.all_fill()


def make_date():
    _dt = datetime.now()
    dt_str = str(_dt.year).zfill(4) + '-' + str(_dt.month).zfill(2) + \
        '-' + str(_dt.day).zfill(2) + '|' + str(_dt.hour).zfill(2) + \
        ':' + str(_dt.minute).zfill(2) + ':' + str(_dt.second).zfill(2)

    return dt_str

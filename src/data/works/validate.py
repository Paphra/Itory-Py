
def _val(val):
    if len(val) > 0:
        try:
            int(val)
            return True
        except (ValueError, TypeError):
            return False
    return False


_variable = None
_prev_v = None


def _prev(event):
    global _prev_v
    _prev_v = _variable.get()


def _now(event):
    global _variable
    if not _val(_variable.get()):
        _variable.set(_prev_v)


def int_(entry, variable):
    global _variable
    _variable = variable
    entry.bind('<KeyPress>', _prev)
    entry.bind('<KeyRelease>', _now)

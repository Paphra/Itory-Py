class Validate:

    def __init__(self, var_, entry_):

        self._prev = self._cur = None

        self._entry = entry_
        self._var = var_
        self._max = None
        self._min = None
        self._min_len = None
        self._max_len = None

    def int_(self, max_: int = None, min_: int = None,
             min_len_: int = None, max_len_: int = None):
        if max_ is not None:
            self._max = max_
        if min_ is not None:
            self._min = min_
        if min_len_ is not None:
            self._min_len = min_len_
        if max_len_ is not None:
            self._max_len = max_len_

        self._entry.bind('<KeyPress>', self._save_prev)
        self._entry.bind('<KeyRelease>', self._work_current)
        self._entry.bind('<FocusOut>', self._work_current_focus)

    def _save_prev(self, event=None):
        self._prev = self._var.get()

    def _work_current(self, event=None):
        self._cur = self._var.get()
        if not self.is_int():
            self._var.set(self._prev)
        if self._max is not None and len(self._cur) > 0 and \
                int(self._cur) > self._max:
            self._var.set(self._max)

        if self._max_len is not None and len(self._cur) > self._max_len:
            self._var.set(self._prev)

        if len(self._cur) == 0:
            self._var.set('0')

    def _work_current_focus(self, event=None):
        self._cur = self._var.get()
        if (self._min is not None and len(self._cur) > 0 and
            int(self._cur) < self._min) or \
                (self._min is not None and len(self._cur) == 0):
            self._var.set(self._min)
        if self._min_len is not None and len(self._cur) < self._min_len:
            self._var.set(self._cur.zfill(self._min_len))

    def is_int(self):
        try:
            self._cur = self._var.get()
            if len(self._cur) > 0:
                int(self._cur)
            return True
        except (ValueError, TypeError):
            return False

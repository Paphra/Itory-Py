from tkinter import messagebox as msg_box


class Confirm:

    def __init__(self):
        self.msg_box = msg_box
        self._title = 'Itory Business Operator'

    def show(self, msg_: str):
        return self.msg_box.askokcancel(self._title,
                                        msg_)

    def show_yes_no(self, msg_: str):
        return self.msg_box.askquestion(self._title, msg_)

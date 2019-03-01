
import tkinter as tk
from tkinter import ttk
from .loginas import LogInAs
from .employees import Employees
from .networth import NetWorth
from .promotions import Promotions
from .suppliers import Suppliers
from .contacts import Contacts


class MainMan(LogInAs, Employees, NetWorth, Promotions, Suppliers, Contacts):

    def __init__(self, container, _sb, man_inst):
        self.host = container
        self.sb = _sb
        self.inst = man_inst

        LogInAs.__init__(self)
        Employees.__init__(self)
        NetWorth.__init__(self)
        Promotions.__init__(self)
        Suppliers.__init__(self)
        Contacts.__init__(self)

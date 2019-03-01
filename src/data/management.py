"""Management Model"""

from datetime import datetime as dt
from .db_connection import Conn


class Management:

    def __init__(self):
        self.login = self.LogIn()

    class LogIn:

        def __init__(self):
            pass

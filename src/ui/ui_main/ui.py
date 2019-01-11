
from .s_bar import Sbar
from .tab_pane import NtBook


class UImain:

    def __init__(self, root):
        self.root = root
        self.sb = Sbar(self.root)

        self.ntbk = NtBook(self.sb, self.root)

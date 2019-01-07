
from .tab_pane import NtBook
from .s_bar import Sbar


class UImain:

    def __init__(self, root):
        self.root = root
        self.sb = Sbar(self.root)
        
        self.ntbk = NtBook(self.sb, self.root)

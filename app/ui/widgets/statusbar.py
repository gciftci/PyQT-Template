# app\ui\widgets\statusbar.py
from PyQt6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)
        """
        Initialize the status bar.
        """
        self.showMessage("Ready")

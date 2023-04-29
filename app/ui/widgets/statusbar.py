# app\ui\widgets\statusbar.py
from PyQt6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    def __init__(self, parent) -> None:
        """
        Initialize the status bar.

        Args:
            parent: The parent widget.
        """
        super().__init__(parent)
        self.showMessage("Ready")

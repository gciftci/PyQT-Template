# app\ui\widgets\menubar.py
from PyQt6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        """
        Initialize the menu bar.
        """
        file_menu = self.addMenu("File")
        edit_menu = self.addMenu("Edit")
        view_menu = self.addMenu("View")
        help_menu = self.addMenu("Help")

        # Add actions to the menus
        file_menu.addAction(self.parent().topbar.actions["Open"])
        file_menu.addAction(self.parent().topbar.actions["Save"])
        file_menu.addAction(self.parent().topbar.actions["Exit"])

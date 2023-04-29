# app\ui\widgets\menubar.py
from PyQt6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, parent=None) -> None:
        """
        Initialize the menu bar.

        Args:
            parent: The parent widget.
        """
        super().__init__(parent)
        file_menu = self.addMenu("File")
        # edit_menu = self.addMenu("Edit")    # TODO: #5 Create entries for "Edit"
        # view_menu = self.addMenu("View")    # TODO: #4 Create entries for "View"
        # help_menu = self.addMenu("Help")    # TODO: #3 Create entries for "Help"

        # Add actions to the menus
        file_menu.addAction(self.parent().topbar.actions["Open"])
        file_menu.addAction(self.parent().topbar.actions["Save"])
        file_menu.addAction(self.parent().topbar.actions["Exit"])

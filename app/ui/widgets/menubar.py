''' app/ui/widgets/menubar.py '''
from PyQt6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    """
    Initialize the menu bar.

    Args:
        parent: The parent widget.
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        file_menu = self.addMenu("File")
        # edit_menu = self.addMenu("Edit")
        # view_menu = self.addMenu("View")
        # help_menu = self.addMenu("Help")

        # Add actions to the menus
        file_menu.addAction(self.parent().topbar.actions_call["Open"]) # type: ignore
        file_menu.addAction(self.parent().topbar.actions_call["Save"]) # type: ignore
        file_menu.addAction(self.parent().topbar.actions_call["Exit"]) # type: ignore

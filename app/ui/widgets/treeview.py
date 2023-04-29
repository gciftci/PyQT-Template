''' app/ui/widgets/treeview.py '''
from PyQt6.QtWidgets import QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir


class TreeView(QTreeView):
    """
    Initialize the TreeView widget.

    Args:
        parent (QWidget, optional): Parent widget of the TreeView. Defaults to None.
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.file_system_model: QFileSystemModel = QFileSystemModel()
        self.file_system_model.setRootPath(QDir.currentPath())
        self.setModel(self.file_system_model)
        self.setRootIndex(self.file_system_model.index(QDir.currentPath()))
        self.setColumnWidth(0, 100)
        self.setFixedWidth(150)
        self.setSortingEnabled(True)

    def clear_view(self) -> None:
        """
        Clearing the TreeView
        """
        self.destroy(destroySubWindows=True)

# app\ui\widgets\treeview.py
from PyQt6.QtWidgets import QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir, QSize


class TreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        """
        Initialize the Treeview.
        """
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(QDir.currentPath())
        self.setModel(self.file_system_model)
        self.setRootIndex(self.file_system_model.index(QDir.currentPath()))
        self.setColumnWidth(0, 100)
        self.setFixedWidth(150)
        self.setSortingEnabled(True)

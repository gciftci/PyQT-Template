# app\ui\widgets\toolbar.py
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QToolBar, QWidget, QSizePolicy


class ToolBar(QToolBar):
    def __init__(self, parent,
                 orientation: Qt.Orientation = Qt.Orientation.Horizontal,
                 style: Qt.ToolButtonStyle = Qt.ToolButtonStyle.ToolButtonTextUnderIcon,
                 icon_size: tuple[int, int] = (32, 32)) -> None:
        """
        Initialize the toolbar.

        Args:
            parent: The parent widget.
            orientation: The toolbar's orientation.
            style: The toolbar's tool button style.
            icon_size: The toolbar's icon size.
        """
        super().__init__(parent)
        self.actions = {}
        self.setOrientation(orientation)

        self.setToolButtonStyle(style)
        self.setIconSize(QSize(icon_size[0], icon_size[1]))

    def add_button(self, text: str, icon: str, trigger_action) -> None:
        """
        Add a button to the toolbar.

        Args:
            text: The button's text.
            icon: The button's icon.
            trigger_action: The action to be executed when the button is clicked.
        """
        self.actions[text] = QAction(QIcon(icon), text, self)
        self.actions[text].triggered.connect(trigger_action)
        self.addAction(self.actions[text])

    def add_separator(self) -> None:
        """
        Add a separator to the toolbar.
        """
        separator = QWidget(self)
        separator.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.addWidget(separator)

    '''
        TODO: #8 Add option to "stack" toolbars (2 TopToolbars)
        TODO: #9 Add layout-method.
    '''

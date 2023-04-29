''' app/ui/widgets/toolbar.py '''
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QToolBar, QWidget, QSizePolicy


class ToolBar(QToolBar):
    """
    Initialize the toolbar.

    Args:
        parent: The parent widget.
        orientation: The toolbar's orientation.
        style: The toolbar's tool button style.
        icon_size: The toolbar's icon size.
    """

    def __init__(self, parent,
                 orientation: Qt.Orientation = Qt.Orientation.Horizontal,
                 style: Qt.ToolButtonStyle = Qt.ToolButtonStyle.ToolButtonTextUnderIcon,
                 icon_size: tuple[int, int] = (32, 32)) -> None:
        super().__init__(parent)
        self.actions_call = {}
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
        self.actions_call[text] = QAction(QIcon(icon), text, self)
        self.actions_call[text].triggered.connect(trigger_action)
        self.addAction(self.actions_call[text])

    def add_separator(self) -> None:
        """
        Add a separator to the toolbar.
        """
        separator = QWidget(self)
        separator.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.addWidget(separator)

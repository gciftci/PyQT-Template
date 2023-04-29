# app\ui\main_window.py
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit
from ..utils.config import AppConfig
from .widgets.menubar import MenuBar
from .widgets.toolbar import ToolBar
from .widgets.statusbar import StatusBar
from .widgets.treeview import TreeView


class MainWindow(QMainWindow):
    def init(self) -> None:
        """
        Initialize the Main-Window.
        """
        super().init()
        self.initUI()

    def initUI(self) -> None:
        """
        Initialize the user interface.
        """
        # Window-Settings
        self.setWindowTitle(AppConfig.APP_NAME)
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        central_widget.setLayout(layout)

        # Create Widgets
        self.create_treeview()
        self.create_toolbars()
        self.create_edit()

        # Add Widgets to Window
        self.setMenuBar(MenuBar(self))
        self.setStatusBar(StatusBar(self))

        layout.addWidget(self.treeview)
        layout.addWidget(self.editbox, stretch=1)
        layout.addWidget(self.editbox)

    def create_toolbars(self) -> None:
        """
        Creates and adds the top and right toolbars to the main window.
        """
        # Top Toolbar [PyQt6.QtWidgets.QToolBar]
        self.topbar = ToolBar(self,
                              orientation=Qt.Orientation.Horizontal,
                              style=Qt.ToolButtonStyle.ToolButtonTextUnderIcon,
                              icon_size=(24, 24))

        # Top Toolbar Buttons
        self.topbar.add_button("Open", "resources/assets/icons/windows/imageres-10.ico", self.open_file)
        self.topbar.add_button("Save", "resources/assets/icons/windows/shell32-259.ico", self.save_file)
        self.topbar.add_separator()
        self.topbar.add_button("Exit", "resources/assets/icons/windows/shell32-220.ico", self.exit_app)

        # Right Toolbar [PyQt6.QtWidgets.QToolBar]
        self.rightbar = ToolBar(self,
                                orientation=Qt.Orientation.Vertical,
                                style=Qt.ToolButtonStyle.ToolButtonIconOnly,
                                icon_size=(24, 24))

        # Right Toolbar Buttons
        self.rightbar.add_separator()
        self.rightbar.add_button("Privacy", "resources/assets/icons/windows/shell32-167.ico", self.privacy_window)
        self.rightbar.add_button("Settings", "resources/assets/icons/windows/shell32-315.ico", self.settings_window)

        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.topbar)
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, self.rightbar)

    def create_treeview(self) -> None:
        """
        Creates and adds the tree view widget to the main window.
        """
        self.treeview = TreeView(self)

    def create_edit(self) -> None:
        """
        Creates and adds the QTextEdit widget to the main window.
        """
        self.editbox = QTextEdit(self)

    def open_file(self) -> None:
        """
        Event handler for the "Open" button. Displays the "Open File" dialog.
        """
        print("Open")

    def save_file(self) -> None:
        """
        Event handler for the "Save" button. Displays the "Save File" dialog.
        """
        print("Save")

    def exit_app(self) -> None:
        """
        Event handler for the "Exit" button. Closes the application.
        """
        self.close()

    def settings_window(self) -> None:
        """
        Event handler for the "Settings" button. Displays the "Settings" window.
        """

    def privacy_window(self) -> None:
        """
        Event handler for the "Privacy" button. Displays the "Privacy" window.
        """
        print("privacy_window")

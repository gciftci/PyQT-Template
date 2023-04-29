''' app/init.py '''
import sys
from PyQt6.QtWidgets import QApplication
from .ui.main_window import MainWindow
from .utils.config import AppConfig


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    app: QApplication = QApplication(sys.argv)
    AppConfig.initialize()

    window: MainWindow = MainWindow()
    window.show()
    return sys.exit(app.exec())

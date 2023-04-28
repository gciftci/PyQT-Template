# app\init.py
import sys
from PyQt6.QtWidgets import QApplication
from .ui.main_window import MainWindow
from .utils.config import AppConfig


def run() -> int:
    """
    Initialize and run the application.

    Returns:
        int: Exit status code.
    """
    app = QApplication(sys.argv)
    AppConfig.initialize()

    window = MainWindow()
    window.show()
    return sys.exit(app.exec())


if __name__ == "__main__":
    run()

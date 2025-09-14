import sys, os, string, subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal

# ---- Worker thread to search all drives ----
class SearchThread(QThread):
    update = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, program_name):
        super().__init__()
        self.program_name = program_name.lower()
        self._running = True

    def run(self):
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                for root, dirs, files in os.walk(drive):
                    if not self._running:
                        return
                    for file in files:
                        if file.lower() == self.program_name or file.lower().startswith(self.program_name):
                            if file.endswith(".exe"):
                                self.update.emit(os.path.join(root, file))
        self.finished.emit()

    def stop(self):
        self._running = False

# ---- Main GUI ----
class EXEFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows EXE Finder - Multi-Search")
        self.setGeometry(200, 100, 800, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Enter Program Name (e.g., chrome, notepad, vlc):")
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.search_btn = QPushButton("Search")
        layout.addWidget(self.search_btn)

        self.listbox = QListWidget()
        layout.addWidget(self.listbox)

        self.search_btn.clicked.connect(self.start_search)
        self.listbox.itemDoubleClicked.connect(self.open_selected)

        self.thread = None

    def start_search(self):
        program_name = self.entry.text().strip()
        if not program_name:
            QMessageBox.warning(self, "Input Required", "Please enter a program name.")
            return

        # Stop previous thread if running
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()

        # Clear previous search results
        self.listbox.clear()

        # Start new search thread
        self.thread = SearchThread(program_name)
        self.thread.update.connect(self.add_item)
        self.thread.finished.connect(self.search_finished)
        self.search_btn.setEnabled(False)
        self.thread.start()

    def add_item(self, path):
        self.listbox.addItem(path)

    def search_finished(self):
        self.search_btn.setEnabled(True)
        if self.listbox.count() == 0:
            QMessageBox.information(self, "Not Found", "No executable found.")

    def open_selected(self, item):
        path = item.text()
        result = QMessageBox.question(self, "Open File", f"Do you want to open:\n{path}?")
        if result == QMessageBox.StandardButton.Yes:
            try:
                subprocess.Popen(path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open {path}\n{e}")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Exit Confirmation",
            "Do you really want to close this application?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()  # Close the window
        else:
            event.ignore()  # Ignore the close event
# ---- Run the app ----
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EXEFinder()
    window.show()
    sys.exit(app.exec())

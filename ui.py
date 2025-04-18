from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
import sys
import time
import psutil

class StatusSignal(QObject):
    update_status = pyqtSignal(str)

class COREUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C.O.R.E. Interface")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        self.date_label = QLabel(time.strftime("%Y-%m-%d %H:%M:%S"), self)
        self.date_label.setAlignment(Qt.AlignLeft)
        self.date_label.setStyleSheet("color: #ADD8E6;")
        self.date_label.setFont(QFont('Arial', 40))

        self.system_label = QLabel("System Online", self)
        self.system_label.setAlignment(Qt.AlignRight)
        self.system_label.setStyleSheet("color: #ADD8E6;")
        self.system_label.setFont(QFont('Arial', 50))

        self.top_layout.addWidget(self.date_label)
        self.top_layout.addWidget(self.system_label)
        self.main_layout.addLayout(self.top_layout)

        self.circle_label = QLabel("C.O.R.E", self)
        self.circle_label.setAlignment(Qt.AlignCenter)
        self.circle_label.setFont(QFont('Arial', 100, QFont.Bold))
        self.circle_label.setStyleSheet("color: #ADD8E6; border: 3px solid #ADD8E6; border-radius: 100px; padding: 20px;")
        self.main_layout.addWidget(self.circle_label, 1, Qt.AlignCenter)

        self.status_label = QLabel("Status: Idle", self)
        self.status_label.setAlignment(Qt.AlignLeft)
        self.status_label.setStyleSheet("color: #ADD8E6;")
        self.status_label.setFont(QFont('Arial', 50))

        self.cpu_label = QLabel("CPU Usage: 0%", self)
        self.cpu_label.setAlignment(Qt.AlignRight)
        self.cpu_label.setStyleSheet("color: #ADD8E6;")
        self.cpu_label.setFont(QFont('Arial', 50))

        self.bottom_layout.addWidget(self.status_label)
        self.bottom_layout.addWidget(self.cpu_label)
        self.main_layout.addLayout(self.bottom_layout)

        self.mic_button = QPushButton("Mic", self)
        self.mic_button.setStyleSheet("background-color: #ADD8E6; color: white; border-radius: 20px;")
        self.mic_button.setFixedSize(100, 50)
        self.main_layout.addWidget(self.mic_button, 0, Qt.AlignBottom | Qt.AlignHCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)
        self.setLayout(self.main_layout)
        self.show()

        # Initialize status signal
        self.status_signal = StatusSignal()

        # Connect the signal to update status
        self.status_signal.update_status.connect(self.set_status)

    def update_info(self):
        self.date_label.setText(time.strftime("%Y-%m-%d %H:%M:%S"))
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")

    def set_status(self, status_text):
        self.status_label.setText(f"Status: {status_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = COREUI()
    sys.exit(app.exec_())

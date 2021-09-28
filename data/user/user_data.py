from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
loc = loc.replace("\\","/")
path = os.path.join(loc, "user/user-data.json")
with open(path, "r") as file:
	_text = file.read()
data = json.loads(_text)

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setContextMenuPolicy(Qt.NoContextMenu)
class UserDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,450)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setWindowTitle("User-Data")
        self.setStyleSheet("""
		* {
			font-family: verdana;
			background: #eee;
		}
		QLineEdit {
			border: 2px solid #ccc;
			padding: 10px 30px;
		}
		QLineEdit:hover {
			background: #f1f1f1;
		}
		QLineEdit:focus {
			border: 2px solid lightblue;
			background: #f1f1f1;
		}
		QPushButton{
	border: none;
      font-size: 17px;
      padding: 15px 30px;
      background: #ddd;
      image: none;
}
QPushButton:hover {
	background: rgb(10, 82, 190);
	color: #fff;
}
QPushButton:pressed {
	background: rgb(10, 82, 250);
	color: #fff;
}
        """)
        heading = QLabel("""
        <center><h1>User Data - SM FastEdit</h1></center>
		""")
        heading.setFixedHeight(100)
        layout = QVBoxLayout(self)
        self.userName = LineEdit()
        self.userName.setText(data["user-name"])
        self.email = LineEdit()
        self.email.setText(data["user-email"])
        self.password = LineEdit()
        self.password.setText(data["password"])
        self.phoneNumber = LineEdit()
        self.phoneNumber.setText(data["phone"])
        button = QPushButton("Confirm")
        button.clicked.connect(self.close)
        layout.addWidget(heading)
        layout.addWidget(self.userName)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(self.phoneNumber)
        layout.addWidget(button)
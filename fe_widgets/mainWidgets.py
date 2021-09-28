import os
from settings.theme import *
from PyQt5.QtCore import QFile, QUrl, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import * 
from PyQt5.QtWebEngineWidgets import *
from data.stylesheets import *


class Menu(QMenu):
	"""Used this widget for context menu of editor""" 
	def __init__(self, parent=None):
            super().__init__(parent)
            self.setStyleSheet(Theme.MenuDark)
class Button(QPushButton):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setStyleSheet(Theme.DialogButton)
	def set_Text(self, text: str):
		self.setText(text)
class MainWidget(QWidget):
	def __init__(self,parent=None):
	    super().__init__(parent)
	    self.setStyleSheet("""
* {
	image: none;
}
QListWidget
{
    background: #444;
    font-size: 13pt;
    color: #ddd;
    min-width: 500px;
    border-radius: 5px;
    border: 1px solid #666;
}

QListWidget::item {
      background: #444;
	color: #ddd;
}
QListWidget::item:hover {
      background: #555;
	color: #ddd;}
QListWidget::item:selected {
	background: rgb(10, 82, 190);
	color: #fff;
}
QListWidget QScrollBar {
    background: transparent;
    color: #333;
}
QListWidget QScrollBar:vertical {
                    border: none;
                    background: #444;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QListWidget QScrollBar::handle:vertical {
                    background: #555;
                    min-height: 30px;
                    border-radius: 5px;
                }
           QListWidget  QScrollBar::handle:vertical:hover {
                    background: #666;
                }
            QListWidget  QScrollBar::handle:vertical:pressed {
                    background: #777;
                }
              QListWidget QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #444;
                    background: #444;
                }
QListWidget QScrollBar {
    background: transparent;
    color: #333;
}
QListWidget QScrollBar:horizontal {
                    border: none;
                    background: #444;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QListWidget QScrollBar::handle:horizontal {
                    background: #555;
                    min-width: 30px;
                    border-radius: 5px;
                }
           QListWidget  QScrollBar::handle:horizontal:hover {
                    background: #666;
                }
            QListWidget  QScrollBar::handle:horizontal:pressed {
                    background: #777;
                }
              QListWidget QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    border: 2px solid #444;
                    background: #444;
                }
	    """)
class BrowserWindow(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setStyleSheet("""
		QWidget {
			background: #222;
			color: #fff;
		}
		QPushButton{
			border: none;
			color: #fff;
                  font-size: 17px;
                  padding: 6px 20px;
                  background: #222;
			margin: 0;
		}
		QPushButton:hover {
			background: rgb(10, 82, 190);
		}
		QPushButton:pressed {
			background: rgb(10, 82, 250);
		}
		QLineEdit {
			padding: 10px 20px;
			border: none;
			background: #222;
			font-family: verdana;
			font-size: 16px;
		}
		QLineEdit:hover {
			background: #222;
		}
		QLineEdit:focus {
			background: #333;
		}
		""")
		self.toolBar = QToolBar()
		self.toolBar.setContentsMargins(0,0,0,0)
		self.webView = QWebEngineView()
		self.webView.setContextMenuPolicy(Qt.NoContextMenu)
		self.webView.setZoomFactor(1.3)
		layout = QVBoxLayout(self)
		layout.setSpacing(0)
		layout.setContentsMargins(0,0,0,0)
		layout.addWidget(self.toolBar)
		layout.addWidget(self.webView)
		reloadBtn = QPushButton()
		reloadBtn.setText("Reload")
		reloadBtn.clicked.connect(self.webView.reload)
		self.urlBar = QLineEdit()
		self.urlBar.setReadOnly(True)
		self.urlBar.setPlaceholderText("Enter url here...")
		self.goBtn = QPushButton()
		self.goBtn.setText("Go")
		self.toolBar.addWidget(reloadBtn)
		self.toolBar.addWidget(self.urlBar)
		self.toolBar.addWidget(self.goBtn)
		self.urlBar.returnPressed.connect(self.loadTextInUrl)
		self.goBtn.clicked.connect(self.loadTextInUrl)
	def loadTextInUrl(self):
		url = self.urlBar.text()
		self.loadURL(url)
	def loadURL(self, url: str):
		self.webView.load(QUrl(url))
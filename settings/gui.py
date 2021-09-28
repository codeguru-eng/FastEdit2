from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys
import json

def getLocation(a1):
     loc = os.path.dirname(os.path.dirname(a1)) + "/"
     loc2 = loc.replace("\\", "/")
     return loc2
def loadJSON(filename):
	with open(filename, "r") as file:
		_text = file.read()
	return json.loads(_text)

loc = getLocation(os.path.abspath(__file__))

path1 = os.path.join(loc, "settings/settings_folder/settings.fe_settings")
path2 = os.path.join(loc, "settings/settings_folder/console.fe_settings")
path3 = os.path.join(loc, "settings/settings_folder/editor.fe_settings")
path4 = os.path.join(loc, "settings/settings_folder/editorTheme.fe_settings")
path5 = os.path.join(loc, "settings/settings_folder/keybindings.fe_settings")
path6 = os.path.join(loc, "settings/theme.json")

files = {
	"window.settings": path1,
	"console": path2,
	"editor.settings": path3,
	"editor.theme": path4,
	"keymap": path5,
	"theme": path6
}

windowSettings 	= loadJSON(files["window.settings"])
console 		= loadJSON(files["console"])
editorSettings 	= loadJSON(files["editor.settings"])
editorTheme 	= loadJSON(files["editor.theme"])
keymap 			= loadJSON(files["keymap"])
theme 			= loadJSON(files["theme"])

class QLabel(QLabel):
	def  __init__(self, label):
		super().__init__()
		font = QFont()
		font.setPointSizeF(10)
		font.setFamily("verdana")
		self.setFont(font)
		self.setText(label)
class TWidget(QWidget):
	def  __init__(self):
		super().__init__()
		self.setStyleSheet("""
		QWidget {
			background: #eee;
		}
		""")
class Appearance(QWidget):
	def  __init__(self):
		super().__init__()
		self.setStyleSheet("""
		QWidget {
			background: #fff;
			color: #000;
		    padding: 10px;
		    margin: 0px;
		}

		""")
		
		################################
		tab = TWidget()
		layoutF = QVBoxLayout(tab)
		layoutF.setContentsMargins(0,0,0,0)
		layoutF.setSpacing(0)
		tabWidthW = QWidget()
		tabWidthW.setFixedWidth(300)
		layout1 = QHBoxLayout(tabWidthW)
		layout1.setContentsMargins(0,0,0,0)
		layout1.setSpacing(0)
		label = QLabel("Tab Width: ")
		tabWidth = QLineEdit()
		layout1.addWidget(label)
		layout1.addWidget(tabWidth)

		autoIndent = QWidget()
		autoIndent.setFixedWidth(300)
		layout1 = QHBoxLayout(autoIndent)
		layout1.setContentsMargins(0,0,0,0)
		layout1.setSpacing(0)
		label = QLabel("Auto Indent: ")
		autoIntentation = QLineEdit()
		layout1.addWidget(label)
		layout1.addWidget(autoIntentation)

		layoutF.addWidget(tabWidthW)
		layoutF.addWidget(autoIndent)
		###############################
		fontWidget = TWidget()
		layoutF = QVBoxLayout(fontWidget)
		layoutF.setContentsMargins(0,0,0,0)
		layoutF.setSpacing(0)
		fontSize = QWidget()
		fontSize.setFixedWidth(300)
		layout1 = QHBoxLayout(fontSize)
		layout1.setContentsMargins(0,0,0,0)
		layout1.setSpacing(0)
		labelFontSize = QLabel("Font Size: ")
		answer = QLineEdit()
		layout1.addWidget(labelFontSize)
		layout1.addWidget(answer)
		layoutF.addWidget(fontSize)
		################################
		layoutMain = QVBoxLayout(self)
		layoutMain.addWidget(tab)
		layoutMain.addWidget(fontWidget)

class Gui(QMainWindow):
	def __init__(self, parent=None):
		super(Gui, self).__init__(parent)
		self.setWindowTitle("Settings")
		self.setWindowIcon(QIcon("Images/txteditor.png"))
		self.setFixedSize(1000,600)
		###########################################
		mainWidget = QWidget()
		layoutMain = QHBoxLayout(mainWidget)
		splitter = QSplitter()
		layoutMain.addWidget(splitter)
		splitter.setContentsMargins(0,0,0,0)
		navArea = QTabWidget()
		splitter.addWidget(navArea)
		###########################################
		self.setCentralWidget(mainWidget)
		self.navArea 	= navArea
		self.addItemToNavarea()
	def addItemToNavarea(self):
		self.navArea.addTab(Appearance(), "Appearance")
		self.navArea.addTab(QWidget(), "Theme")
		self.navArea.addTab(QWidget(), "Shortcuts")
		self.navArea.addTab(QWidget(), "Console")
		self.navArea.addTab(QWidget(), "Others")
def main():
	app = QApplication(sys.argv)
	win = Gui()
	win.show()
	app.exec_()
if __name__ == '__main__':
	main()
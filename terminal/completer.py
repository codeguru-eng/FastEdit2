from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Command_Completer(QCompleter):
	List = ["print", "input", "import", "from", "class", "def"]
	def __init__(self):
		super(Command_Completer, self).__init__()
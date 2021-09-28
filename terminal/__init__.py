from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from .terminalFunc import *
from settings.theme import *
from settings.font import *
from settings.settings import *
from .highlighter import *
from .completer import Command_Completer

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"

class Terminal(QWidget):
      """Assistant widget"""
      command_history 	= []
      _terminal		= TerminalMain()
      _incomplete		= False
      def __init__(self, parent=None):
          super(Terminal, self).__init__(parent)
          self.commandArea = QLineEdit()
          self.commandArea.setObjectName("commandArea")
          self.commandArea.setPlaceholderText("Command...")
          self.commandArea.returnPressed.connect(self.push)
          self.completer = QCompleter(Command_Completer.List)
          self.commandArea.setCompleter(self.completer)
          self.outputArea  = QPlainTextEdit()
          self.highlighter = Highlighter(self.outputArea.document())
          self.outputArea.moveCursor(QTextCursor.EndOfLine)
          self.outputArea.setReadOnly(True)
          self.outputArea.setObjectName("outputArea")
          font = QFont()
          font.setFamily(FontFamily.Console)
          font.setPointSizeF(FontSize.FontSizeTerminal)
          self.outputArea.setFont(font)
          layout = QVBoxLayout(self)
          layout.addWidget(self.outputArea)
          layout.addWidget(self.commandArea)
          layout.setContentsMargins(0,0,0,0)
          layout.setSpacing(0)
          self.outputArea.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
          self.commandArea.setContextMenuPolicy(Qt.NoContextMenu)
          self.onStart()
      def add_history(self, command):
      	if command == "history()":
      		return
      	self.command_history.append(command)
      def push(self):
            command = self.commandArea.text()
            self.outputArea.moveCursor(QTextCursor.EndOfLine)
            self.add_history(command)
            if command == "history()":
            	self.showCommand()
            	self.showOutput(self.command_history)
            	self.commandArea.clear()
            	return
            if command == "clearHistory()":
            	self.command_history = []
            	self.command_history.clear()
            	self.showCommand()
            	self.showOutput("Cleared history.")
            	self.commandArea.clear()
            	return
            if command == "exit()" or command == "clear()":
                self.outputArea.clear()
                self.commandArea.clear()
                filepath = os.path.join(loc, "data/user/terminal_log.txt")
                log_file = open(filepath, "w+")
                log_file.write(self.outputArea.toPlainText())
                log_file.close()
                return
            if command == "help":
            	self.showCommand()
            	self.showOutput("Type help() for interactive help, or help(object) for help about object.")
            	return
            if command == "help()":
            	self.showCommand()
            	text = """
Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam"."""
            	text = text.splitlines()
            	for i in text:
            		self.showOutput(i)
            	self.commandArea.clear()
            	return
            if "input" in command:
                  self.showCommand()
                  text = """
Traceback (most recent call last):
File "", line 1, in <module>
RuntimeError: input(): lost sys.stdin"""
                  text = text.splitlines()
                  for i in text:
                        self.showOutput(i)
                  self.commandArea.clear()
                  self.showCommand()           
                  return
            incomplete = self._terminal.push(command)
            if not incomplete:
            	output = self._terminal.output.splitlines()
            	self._incomplete = False
            	if output:
            		self.showCommand()
            		for line in output:
            			self.showOutput(line)
            	else:
            		self.showLi(command)
            else:
            	if not self._incomplete:
            		self._incomplete = True
            self.commandArea.clear()
      def userName(self):
            text = self.parent.username
            return text
      def tell(self, text):
            self.outputArea.appendHtml(f"<span style='color:#158cee;'></span> {text}")
      def showCommand(self):
      	__text = self.commandArea.text()
      	self.outputArea.appendHtml(f"<span style='color:#158cee;'>>>></span> {__text}")
      def showOutput(self, text):
            self.outputArea.appendHtml(f"{text}")
      def showLi(self, text):
            self.outputArea.appendHtml(f"<span style='color:#158cee;'>>>></span> {text}")
      def onStart(self):
            """
            Open terminal with the same text saved in terminal_log.txt file.
            """
            filepath = os.path.join(loc, "data/user/terminal_log.txt")
            log_file = open(filepath, "r")
            text = log_file.read()
            self.outputArea.setPlainText(text)

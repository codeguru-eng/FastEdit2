from settings.theme import *
from settings.font import *
from settings.settings import *
from data.stylesheets import *
from .assistant import *
from terminal import *
from .problems import *
import methods
from PyQt5.QtWidgets import QAbstractScrollArea, QLabel, QLineEdit, QListWidget, QPlainTextEdit, QTabWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication, QProcess, QSize, Qt
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/settings_folder/console.fe_settings")
with open(path, "r") as file:
      _text = file.read()
data = json.loads(_text)
if data["Run"]["OpenHTMLFileInBuiltinBrowser"] is True:
      OpenHTMLInBuiltinBrowser = True
elif data["Run"]["OpenHTMLFileInBuiltinBrowser"] is False:
      OpenHTMLInBuiltinBrowser = False
class Output(QPlainTextEdit):
      def __init__(self):
            # variables
            #############
            super().__init__()
            self.setUndoRedoEnabled(False)
            self.setCursorWidth(data["Console"]["CaretWidth"])
            self.moveCursor(QTextCursor.EndOfLine)
            font = QFont()
            font.setFamily(FontFamily.Console)
            font.setPointSizeF(FontSize.FontSizeTerminal)
            self.setFont(font)
            self.setContextMenuPolicy(Qt.NoContextMenu)
            self.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
            self.setReadOnly(data["Console"]["ReadOnlyMode"])
            self.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
            self.horizontalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
class ConsoleWidget(QTabWidget):
      def __init__(self):
            super().__init__()
            self.setMinimumHeight(data["Console"]["MinHeight"])
            self.setMaximumHeight(data["Console"]["MaxHeight"])
            self.setMovable(False)
            self.setTabPosition(QTabWidget.North)
            self.setIconSize(QSize(25,25))
            a = self.addTab(Output(), "Output")
            self.setTabIcon(a, QIcon("Images\\Icons\\iconOutput.png"))
            self.setTabToolTip(a, "Output")
            b = self.addTab(Assistant(), "Assistant")
            self.setTabIcon(b, QIcon("Images\\Icons\\iconAssistant.png"))
            self.setTabToolTip(b, "Assistant")
            c = self.addTab(Problems(), "Problems")
            self.setTabIcon(c, QIcon("Images\\Icons\\iconProblem.png"))
            self.setTabToolTip(c, "Problems")
            d = self.addTab(Terminal(), "Terminal")
            self.setTabIcon(d, QIcon("Images\\Icons\\iconTerminal.png"))
            self.setTabToolTip(d, "Terminal")
            self.output = self.widget(a)
            self.assistant = self.widget(b).outputArea
            self.askField = self.widget(b).commandArea
            self.assistantM = self.widget(b)
            self.problems = self.widget(c)
            self.terminal = self.widget(d)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Outline(QListWidget):
    def __init__(self, parent=None):
        super(Outline, self).__init__(parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
        self.horizontalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
        self.itemClicked.connect(self.gotoElement)
    def makeOutlineList(self, text=''):
        edict = {}
        textList = text.splitlines()
        i = 1
        for x in textList:
            if x.strip().startswith('class ') or x.strip().startswith('def ') or x.strip().startswith('import ') or x.strip().startswith('from '):
                edict[i] = x.strip() 
            i += 1
        return edict
    def update(self, edict):
        self.clear()
        self.code = list(edict.values())
        self.linenumbers = list(edict.keys())
        for line in self.code:
            if line.strip().startswith('class'):
                item = QListWidgetItem()
                text = line.strip()
                text = text.strip(':')
                item.setText(f"{text}")
                item.setIcon(QIcon("Images/Icons/iconClassDark.png"))
                self.addItem(item)
            elif line.strip().startswith('def'):
                item = QListWidgetItem()
                text = line.strip()
                text = text.strip(':')
                item.setText(f'  {text}')
                item.setIcon(QIcon("Images/Icons/iconFuncDark.png"))
                self.addItem(item)
            elif line.strip().startswith('from'):
                item = QListWidgetItem()
                text = line.strip()
                text = text.strip(':')
                item.setText(f'{text}')
                self.addItem(item)
            elif line.strip().startswith('import'):
                item = QListWidgetItem()
                text = line.strip()
                text = text.strip(':')
                item.setText(f'{text}')
                self.addItem(item)
    def gotoElement(self):
        row = self.currentRow() 
        linenumber = self.linenumbers[row] - 1
        editor = self.parent.tabWidget.currentWidget()
        if linenumber >= 0:
            y = editor.lineLength(linenumber) - 1
            editor.setCursorPosition(linenumber, y)
            editor.setFocus()
        self.clearSelection()
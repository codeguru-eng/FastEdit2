from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

class Fe_Editor(QsciScintilla):
      def __init__(self, parent=None):
            super().__init__(parent)
      def delete(self):
            self.SendScintilla(QsciScintilla.SCI_CLEAR)
      def _cut(self):
            """Method to cut selected text."""
            if self.hasSelectedText():
                  self.removeSelectedText()
      def _copy(self):
            """Copy selected text"""
            self.copy()
      def _paste(self):
            self.paste()
      def _undo(self):
            if self.isUndoAvailable():
                  self.undo()
      def _redo(self):
            if self.isRedoAvailable():
                  self.redo()

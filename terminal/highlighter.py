from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        errorFormat = QTextCharFormat()
        errorFormat.setForeground(QColor("red"))

        operatorFormat = QTextCharFormat()
        operatorFormat.setForeground(QColor("#158cee"))

        numberFormat = QTextCharFormat()
        numberFormat.setForeground(QColor("violet"))

        errorPatterns = [
            "\\bNameError\\b", "\\bSyntaxError\\b", "\\bRuntimeError\\b","\\bAssertionError\\b",
            "\\bAttributeError\\b","\\bEOFError\\b","\\bFloatingPointError\\b","\\bNameError\\b", 
            "\\bSyntaxError\\b", "\\bRuntimeError\\b","\\bGeneratorExit\\b","\\bImportError\\b",
            "\\bIndexError\\b","\\bKeyError\\b", "\\bKeyboardInterrupt\\b","\\bMemoryError\\b","\\bNameError\\b",
            "\\bNotImplementedError\\b","\\bIndentationError\\b","\\bTabError\\b","\\bSystemError\\b","\\bTypeError\\b",
            "\\bFastEditError\\b"
        ]
        pattern1 =     '\\b[+-]?[0-9]+[lL]?\\b'
        pattern2 =     '\\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\\b'
        pattern3 =     '\\b[+-]?[0-9]+(?:\\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\\b'

        operators = ['=','==', '!=', '<', '<=', '>', '>=','\\+', '-', '\\*', '/', '//', '\\%', '\\*\\*','\\+=', '-=', '\\*=', '/=', '\\%=','\\^', '\\|', '\\&', '\\~', '>>', '<<']

        self.highlightingRules = [
            (QRegExp(pattern), errorFormat) for pattern in errorPatterns
        ]
        self.highlightingRules.append((QRegExp(pattern1), numberFormat))
        self.highlightingRules.append((QRegExp(pattern2), numberFormat))
        self.highlightingRules.append((QRegExp(pattern3), numberFormat))
        for pattern in operators:
            self.highlightingRules.append((QRegExp(pattern), operatorFormat))

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
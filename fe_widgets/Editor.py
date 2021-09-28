from PyQt5 import QtCore
import PyQt5
from PyQt5.Qt import Qt
from PyQt5.Qsci import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QClipboard, QColor, QFont, QFontMetrics
from PyQt5.QtWidgets import QApplication, QMenu
from .mainWidgets import *
import platform
from data.fe_classes import Fe_Editor
from settings.font import *
from settings.shortcuts import *
from settings.theme import *
from settings.syntaxC import *
from data.autocompletion.pyqt5List import Modules, Widgets
from data.autocompletion.pyKeywords import Keywords
from data.autocompletion.jsKeywords import *
from data.autocompletion.pyMethods import *
from data.autocompletion.cssExtra import *
from data.autocompletion.htmlExtra import *
from data.autocompletion.jsonLists import *
from data.calltips.python import *
from settings.editorsettings import *
from methods import *
import resources
import json
import re

# Variable
tagsC = QColor(HtmlTag)
commentC = QColor(Comment)
attrC = QColor(HtmlAtr)
strC = QColor(String)
marginC = Theme.EditorBG
keyWordC = QColor(Keyword)

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "data/api/addApi.fe_settings")
with open(path, "r") as file:
    _text = file.read()
data = json.loads(_text)
mainText = ""
loc = getLocation(os.path.abspath(__file__))

class LexerJS(QsciLexerJavaScript):
      def __init__(self):
            super().__init__()
            # adding let keyword to lexer
      def keywords(self, index):
            keywords = QsciLexerJavaScript.keywords(self, index) or ''
            if index == 1:
                  return  ' let ' + keywords
                  
class LexerPython(QsciLexerPython):
      def __init__(self):
            super().__init__()
      # adding extra keywords to lexer
      def keywords(self, index):
            keywords = QsciLexerPython.keywords(self, index) or ''
            if index == 1:
                  return  ' len ' + ' __name__ ' + ' str ' + ' int ' + ' float ' + ' self ' + ' __peg_parser__ ' + ' await ' + ' nonlocal ' + ' True ' + ' False ' + keywords
 # editor area
class Editor(Fe_Editor):
      """Editor Widget"""
      selection_lock          = None
      selection_indicator     = 4
      multi_cursor_editing    = False
      isPythonFile            = None
      isHTMLFile              = None
      isCSSFile               = None
      isJSONFile              = None
      isSettingFile           = None
      matching_pairs          = [
            '()', 
            '[]',
            '{}',
            '<>',
            "''",
            '""'
      ]
      matching_pairs2          = [
            '()', 
            '[]',
            '{}',
            '<>',
            "''",
            '""',
            ":;"
      ]
      if_name                 = """\ndef main():\n    # Code here...\n\nif __name__ == "__main__":\n\tmain()"""
      from_imp                = """from module import *"""

      # regex
      import_r                = re.compile(r"^[ \t]*from [\w.]+ ")
      doctype_r               = re.compile(r"^[ \t]*<!doctype+ ")
      U_doctype_r             = re.compile(r"^[ \t]*<!DOCTYPE+ ")
      def_r                   = re.compile(r"^[ \t]*(def|cdef|cpdef) \w+\(")
      class_r                 = re.compile(r"^[ \t]*(cdef[ \t]+)?class \w+\(")
      list_css_r              = [
            re.compile(r"^[ \t]*body+ "), 
            re.compile(r"^[ \t]*button+ "), 
            re.compile(r"^[ \t]*a+ "), 
            re.compile(r"^[ \t]*link+ "),
            re.compile(r"^[ \t]*html+ "),
            re.compile(r"^[ \t]*div+ "),
            re.compile(r"^[ \t]*h1+ "),
            re.compile(r"^[ \t]*h2+ "),
            re.compile(r"^[ \t]*h3+ "),
            re.compile(r"^[ \t]*h4+ "),
            re.compile(r"^[ \t]*h5+ "),
            re.compile(r"^[ \t]*p+ "),
            re.compile(r"^[ \t]*form+ "),
            re.compile(r"^[ \t]*input+ "),
            re.compile(r"^[ \t]*img+ ")
      ]

      # signals
      backspacePressed__      = pyqtSignal()
      def keyPressEvent(self, event):
            """This method will decide what to do after given keys are pressed."""
            line = self.getCursorPosition()[0]
            col = self.getCursorPosition()[1]
            if event.key() == Qt.Key_Backspace:
                  self.backspacePressed__.emit()
            if MagicTyping is True:
                  if self.isPythonFile():
                        if event.key() == Qt.Key_F2:
                              self.insert(self.if_name)
                              self.setSelection(line+2, col+4, line+2, col + 18)
                        elif event.key() == Qt.Key_F3:
                              self.insert(self.from_imp)
                              self.setSelection(line, col+5, line, col + 11)
                  if self.isCSSFile():
                        if event.key() == Qt.Key_Backspace:
                              text = self.text(line)[col - 1:col + 1]
                              if text in self.matching_pairs2:
                                    self.delete()
            super(Editor, self).keyPressEvent(event)

      def __init__(self, parent=None):
            super(Editor, self).__init__(parent)
            self.setStyleSheet("border: none;")
            # editor
            self.setSelectionBackgroundColor(Selection.ColorBG)
            self.resetSelectionForegroundColor()
            # signals
            self.textChanged.connect(self.unsaved)
            self.textChanged.connect(self.__textChanged)
            self.textChanged.connect(self._textChanged)
            self.selectionChanged.connect(self.onSelection)
            self.selectionChanged.connect(self._onSelection)
            self.linesChanged.connect(self.lineChanged_)
            self.selectionChanged.connect(self.getSelectedCharNum)
            self.SCN_CHARADDED.connect(self.character_added)
            self.backspacePressed__.connect(self.backspacePressed)
            # variables
            self.saved              = False # saved file or not
            self.path               = None  # file path or not
            self.selection_lock     = False 
            self.savable            = True  # can be save or not
            # font
            self.fontM = QFont()
        
            #system = platform.system().lower()
            #if system == 'windows':
                  #self.fontM.setFamily(FontFamily.Editor)
            #else:
                  #self.fontM.setFamily(FontFamily.Editor)
        
            self.fontM.setFixedPitch(True)
            self.fontM.setPointSizeF(FontSize.FontSizeF)
            self.setFont(self.fontM)
            self.setMarginsFont(self.fontM)
            # match braces 
            self.setMatchedBraceBackgroundColor(BraceMatchingBackgroundColor)
            self.setMatchedBraceForegroundColor(Theme.EditorC)
            self.setUnmatchedBraceBackgroundColor(Theme.EditorBG)
            self.setUnmatchedBraceForegroundColor(QColor(UnclosedString))
            self.setBraceMatching(BraceMatching)
            # wrap
            self.setWhitespaceVisibility(QsciScintilla.WsVisible)
            self.setWhitespaceBackgroundColor(Theme.EditorBG)
            self.setWhitespaceForegroundColor(QColor("#666"))
            self.SendScintilla(QsciScintilla.SCI_SETINDENTATIONGUIDES, QsciScintilla.SC_IV_LOOKFORWARD)
            self.setIndentationGuidesBackgroundColor(QColor("#666"))
            self.setTabDrawMode(QsciScintilla.TabStrikeOut)
            # font
            self.fontM = QFont()
            self.fontM.setFamily(FontFamily.Editor)
            self.fontM.setPointSizeF(FontSize.FontSizeF)
            self.setFont(self.fontM)
            self.setMarginsFont(self.fontM)
            # line number bar
            self.setMarginWidth(0, "0000")
            self.setMarginLineNumbers(0, LineNumbersVisible)
            self.setMarginsForegroundColor(Theme.LineNumberC)
            self.setMarginsBackgroundColor(Theme.EditorBG)
            self.setMarginOptions(QsciScintilla.MoSublineSelect)
            # context menu
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.customContextMenu)
            # caret
            self.SendScintilla(QsciScintilla.SCI_SETCARETFORE, QColor('#ffffff'))
            self.setCaretWidth(Caret.CaretWidth)
            self.setCaretLineBackgroundColor(QColor.fromRgbF(Caret.CaretBColorR,Caret.CaretBColorG,Caret.CaretBColorB, Caret.CaretBColorA))
            self.setCaretForegroundColor(QColor(Caret.CaretColor))
            self.setCaretLineVisible(True)
            self.SendScintilla(QsciScintilla.SCI_SETCARETSTYLE, Caret.CaretStyle)
            # Scroll bar
            self.verticalScrollBar().setStyleSheet(Theme.VScrollBar)
            self.cornerwidget = QLabel("")
            self.setCornerWidget(self.cornerwidget)
            self.horizontalScrollBar().setStyleSheet(Theme.HScrollBar)
            self.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
            self.horizontalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
            # tab size
            self.tWidth = 4
            self.setTabWidth(self.tWidth)
            self.cursorPositionChanged.connect(self.getlineAndCol)
            self.style = None
            # parent
            self.setHighlightingFor("text")
            self.setUtf8(True)
            self.setOverwriteMode(OverWriteMode)
            self.setMarginSensitivity(0, LineNumberSenstivity)
            self.setAutoIndent(Indent.AutoIndent)
            self.setIndentationsUseTabs(Indent.IndentuseTabs)
            self.setText(mainText) 
            self.setBackspaceUnindents(Indent.BackSpaceUnIndent)
            self.setAcceptDrops(AcceptDrops)
            self.setEolMode(QsciScintilla.EolUnix)
            self.setPaper(Theme.EditorBG)
            self.setMarkerBackgroundColor(QColor("#555"))
            self.setMarkerForegroundColor(QColor("#555"))
            self.setFoldMarginColors(QColor(FoldArea), QColor(FoldArea))
            self.setFold()
            self.registerImage(4, QImage.scaled(QImage("Images\\Icons\\iconFunc.png"), 100,100, Qt.KeepAspectRatio))
            self.registerImage(1, QImage.scaled(QImage("Images\\Icons\\iconClass.png"), 100,100, Qt.KeepAspectRatio))
            self.registerImage(2, QImage.scaled(QImage("Images\\Icons\\iconKeyword.png"), 100,100,Qt.KeepAspectRatio))
            self.registerImage(3, QImage.scaled(QImage("Images\\Icons\\iconColor.png"), 100,100,Qt.KeepAspectRatio))
            self.registerImage(5, QImage.scaled(QImage("Images\\Icons\\iconSuggest.png"), 100,100,Qt.KeepAspectRatio))
            self.setAcceptDrops(True)
            if self.hasSelectedText():
                  self.getSelectedCharNum()
            if Selection.MultiCursorEditing == True:
                  self.setMultiCursorEditing()
            self.parseStylesheet()
      def backspacePressed(self):
            line = self.getCursorPosition()[0]
            col = self.getCursorPosition()[1]
            text = self.text(line)[col - 1:col + 1]
            if text in self.matching_pairs:
                  self.delete()
      def _textChanged(self):
            if self.path:
                  self.parent.setAutoSave()
                  pass
      def __textChanged(self):
            if self.parent.tabWidget.currentWidget():
                  if self.path:
                        if self.parent.tabWidget2.currentWidget():
                              if self.parent.tabWidget2.currentWidget().path == self.path:
                                    line, col = self.parent.tabWidget.currentWidget().getCursorPosition()
                                    self.parent.tabWidget2.currentWidget().setText(self.text())
                                    self.parent.tabWidget2.currentWidget().setCursorPosition(line, col)
      def parseStylesheet(self):
            sty = """
            QLabel {
                  background: #222;
            }
            """
            self.cornerwidget.setStyleSheet(sty)
      def setMultiCursorEditing(self):
            try:
                  self.multi_cursor_editing = True
                  self.SendScintilla(QsciScintilla.SCI_SETMULTIPLESELECTION, True)
                  self.SendScintilla(QsciScintilla.SCI_SETMULTIPASTE, 1)
                  self.SendScintilla(QsciScintilla.SCI_SETADDITIONALSELECTIONTYPING, True)
                  self.parent.btn1.setText("MultiCursorEditing")
            except Exception as e:
                  print(str(e))
      def backspace(self):
            self.editorCommand(QsciScintilla.SCI_DELETEBACK)
      def lineChanged_(self):
            self.updateMarginWidth()
      def updateMarginWidth(self):
            """Update margin width if line numbers increased."""
            line_count  = self.lines()
            self.setMarginWidth(0, str(line_count) + "000")
      def _onSelection(self):
            if self.hasSelectedText() is True:
                  self.setCaretLineBackgroundColor(Editor_Dark)
      def reloadFile(self):
            self.parent.reloadFile()
            pass
      def unsaved(self):
            self.saved = False
            self.savable = True
            self.parent.btn2.setText("Unsaved")
      def customContextMenu(self, point):
            self.menu = Menu()
            undo = self.menu.addAction("Undo")
            undo.triggered.connect(self._undo)
            redo = self.menu.addAction("Redo")
            redo.triggered.connect(self._redo)
            self.menu.addSeparator()
            cut = self.menu.addAction("Cut")
            cut.triggered.connect(self._cut)
            copy = self.menu.addAction("Copy")
            copy.triggered.connect(self._copy)
            paste = self.menu.addAction("Paste")
            paste.triggered.connect(self._paste)
            self.menu.addSeparator()
            select_all = self.menu.addAction("Select All")
            select_all.triggered.connect(self.selectAllText)
            copy_all = self.menu.addAction("Copy All")
            copy_all.triggered.connect(self.copyAll)
            self.menu.addSeparator()
            copyLine = self.menu.addAction("Copy Line")
            copyLine.setShortcut("Ctrl+C")
            copyLine.triggered.connect(self.copy_line)
            deleteLine = self.menu.addAction("Delete Line")
            deleteLine.triggered.connect(self.delete_line)
            self.menu.addSeparator()
            self.showSplitViewAct()
            ########################################
            undo.setShortcut(ShortcutKeys.Undo)
            redo.setShortcut(ShortcutKeys.Redo)
            cut.setShortcut(ShortcutKeys.Cut)
            copy.setShortcut(ShortcutKeys.Copy)
            paste.setShortcut(ShortcutKeys.Paste)
            select_all.setShortcut(ShortcutKeys.SelectAll)
            copy_all.setShortcut(ShortcutKeys.CopyAll)
            deleteLine.setShortcut(ShortcutKeys.DeleteLine)
            ########################################
            self.menu.exec_(self.mapToGlobal(point))
      def showSplitViewAct(self):
            if self.parent.tabWidget.currentWidget() == self:
                  if self.path is None:
                        return
                  elif self.path in getFiles.filesList:
                        if self.path == getFiles.path1:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path1D))
                        elif self.path == getFiles.path2:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path2D))
                        elif self.path == getFiles.path3:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path3D))
                        elif self.path == getFiles.path4:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path4D))
                        elif self.path == getFiles.path5:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path5D))
                        elif self.path == getFiles.path7:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path7D))
                        elif self.path == getFiles.path8:
                              openInSplitView = self.menu.addAction("Open Default Settings")
                              openInSplitView.triggered.connect(lambda: self.openInSplitView(getFiles.path8D))
                  else:
                        openInSplitView = self.menu.addAction("Split View")
                        openInSplitView.triggered.connect(lambda: self.openInSplitView(self.path))
      def openInSplitView(self, path):
            if self.parent.tabWidget2.isHidden():
                  self.parent.openInSplitView(path)
                  self.parent.tabWidget2.show()
            elif self.parent.tabWidget2.isVisible():
                  self.parent.openInSplitView(path)
      def copy_line(self):
            self.SendScintilla(QsciCommand.LineCopy)
      def delete_line(self):
            self.SendScintilla(QsciCommand.LineDelete)
      def selectAllText(self):
            self.selectAll()
      def copyAll(self):
            self.selectAll()
            self._copy()
      def setHighlightingFor(self, lang: str):
            if lang == "text" or lang == "plain text":
                  self.style = None
                  self.setLexer(None)
                  self.setPaper(Theme.EditorBG)
                  self.setColor(Theme.EditorC)
            elif lang == "html" or lang == "HTML":
                  self.setAutoIndent(True)
                  self.style = "HTML"
                  font1 = QFont()
                  font1.setItalic(True)
                  font1.setFamily(FontFamily.Editor)
                  font1.setPointSizeF(FontSize.FontSizeF)
                  font2 = QFont()
                  font2.setFamily(FontFamily.Editor)
                  font2.setPointSizeF(FontSize.FontSizeF)
                  lexer = QsciLexerHTML(self)
                  self.setPaper(Theme.EditorBG)
                  self.setColor(Theme.EditorC)
                  self.fontM = QFont()
                  self.fontM.setFamily(FontFamily.Editor)
                  self.fontM.setPointSizeF(FontSize.FontSizeF)
                  lexer.setDefaultFont(self.fontM)
                  lexer.setDefaultPaper(Theme.EditorBG)
                  lexer.setDefaultColor(Theme.EditorC)
                  lexer.setColor(QColor(DefaultColor), QsciLexerHTML.Default)
                  lexer.setFont(self.fontM, QsciLexerHTML.Default)
                  lexer.setMakoTemplates(True)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.Default)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.PHPKeyword)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.PHPOperator)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.XMLEnd)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.XMLTagEnd)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.PHPDefault)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.PHPDefault)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptDefault)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptDefault)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptCommentLine)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptCommentDoc)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptComment)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptCommentLine)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptCommentLine)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptCommentDoc)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptUnclosedString)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptCommentDoc)
                  lexer.setColor(QColor("#5eb1ff"), QsciLexerHTML.JavaScriptKeyword)
                  lexer.setFont(font1, QsciLexerHTML.JavaScriptKeyword)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptKeyword)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptDefault)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptDefault)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptDefault)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptDefault)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptCommentDoc)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptComment)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptCommentLine)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptComment)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptDoubleQuotedString)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptDoubleQuotedString)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptDoubleQuotedString)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptComment)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptDoubleQuotedString)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptSingleQuotedString)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptSingleQuotedString)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptSingleQuotedString)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptUnclosedString)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptUnclosedString)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptNumber)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptNumber)
                  lexer.setColor(QColor(Number), QsciLexerHTML.JavaScriptNumber)
                  lexer.setColor(QColor(Comment), QsciLexerHTML.JavaScriptSymbol)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptSymbol)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptRegex)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptRegex)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptStart)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptStart)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.JavaScriptWord)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.JavaScriptWord)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptWord)
                  lexer.setFont(self.fontM, QsciLexerHTML.JavaScriptSymbol)
                  lexer.setFont(self.fontM, QsciLexerHTML.Default)
                  lexer.setColor(tagsC, QsciLexerHTML.Tag)
                  lexer.setColor(commentC, QsciLexerHTML.HTMLComment)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.HTMLComment)
                  lexer.setFont(font1, QsciLexerHTML.HTMLComment)
                  lexer.setFont(font1, QsciLexerHTML.SGMLComment )
                  lexer.setColor(tagsC, QsciLexerHTML.SGMLDefault )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLDefault )
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLDefault )
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.CDATA)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.CDATA)
                  lexer.setFont(self.fontM, QsciLexerHTML.CDATA)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.SGMLBlockDefault )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLBlockDefault )
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLBlockDefault )
                  lexer.setColor(QColor("#5eb1ff"), QsciLexerHTML.SGMLParameter)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLParameter)
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLParameter)
                  lexer.setColor(tagsC, QsciLexerHTML.SGMLCommand)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLCommand)
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLCommand)
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.SGMLSpecial )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLSpecial )
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLSpecial )
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.SGMLError  )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLError  )
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLError  )
                  lexer.setColor(Theme.EditorC, QsciLexerHTML.SGMLParameterComment   )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLParameterComment   )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLDoubleQuotedString   )
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.SGMLSingleQuotedString   )
                  lexer.setFont(self.fontM, QsciLexerHTML.SGMLParameterComment   )
                  lexer.setFont(font1, QsciLexerHTML.Attribute)
                  lexer.setColor(attrC, QsciLexerHTML.Attribute)
                  lexer.setFont(font1, QsciLexerHTML.UnknownAttribute)
                  lexer.setColor(attrC, QsciLexerHTML.UnknownAttribute)
                  lexer.setColor(QColor(HtmlString), QsciLexerHTML.HTMLDoubleQuotedString)
                  lexer.setColor(QColor(HtmlString), QsciLexerHTML.HTMLSingleQuotedString)
                  lexer.setColor(QColor(HtmlString), QsciLexerHTML.SGMLDoubleQuotedString )
                  lexer.setColor(QColor(HtmlString), QsciLexerHTML.SGMLSingleQuotedString )
                  lexer.setColor(QColor(HtmlString), QsciLexerHTML.HTMLNumber)
                  lexer.setColor(QColor(HtmlEntity), QsciLexerHTML.Entity)
                  lexer.setFont(font2, QsciLexerHTML.Entity)
                  lexer.setColor(tagsC, QsciLexerHTML.OtherInTag)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.OtherInTag)
                  lexer.setColor(tagsC, QsciLexerHTML.UnknownTag)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.UnknownTag)
                  lexer.setColor(attrC, QsciLexerHTML.UnknownAttribute)
                  lexer.setColor(QColor(HtmlValue), QsciLexerHTML.HTMLValue)
                  lexer.setPaper(Theme.EditorBG, QsciLexerHTML.HTMLValue)
                  lexer.setFoldCompact(False)
                  self.lexerHTML = lexer
                  self.setHtmlAutoComplete()
                  self.setLexer(lexer)
            elif lang == "css" or lang == "CSS":
                  self.setAutoIndent(True)
                  self.style = "CSS"
                  font1 = QFont()
                  font1.setBold(False)
                  font1.setFamily(FontFamily.Editor)
                  font1.setPointSizeF(FontSize.FontSizeF)
                  font2 = QFont()
                  font2.setItalic(True)
                  font2.setFamily(FontFamily.Editor)
                  font2.setPointSizeF(FontSize.FontSizeF)
                  lexerCSS = QsciLexerCSS(self)
                  lexerCSS.setDefaultFont(font1)
                  lexerCSS.setDefaultPaper(Theme.EditorBG)
                  lexerCSS.setDefaultColor(Theme.EditorC)
                  lexerCSS.setColor(Theme.EditorC, QsciLexerCSS.Default)
                  lexerCSS.setColor(QColor(cssTag), QsciLexerCSS.Tag)
                  lexerCSS.setFont(font1, QsciLexerCSS.Tag)
                  lexerCSS.setColor(Theme.EditorC, QsciLexerCSS.Operator)
                  lexerCSS.setPaper(Theme.EditorBG, QsciLexerCSS.Operator)
                  lexerCSS.setColor(QColor(cssAtr), QsciLexerCSS.Attribute)
                  lexerCSS.setColor(QColor(cssProperty), QsciLexerCSS.CSS1Property)
                  lexerCSS.setColor(QColor(cssProperty), QsciLexerCSS.CSS2Property)
                  lexerCSS.setColor(QColor(cssProperty), QsciLexerCSS.CSS3Property)
                  lexerCSS.setColor(QColor(cssProperty), QsciLexerCSS.UnknownProperty)
                  lexerCSS.setColor(QColor(cssValue), QsciLexerCSS.Value)
                  lexerCSS.setColor(strC, QsciLexerCSS.SingleQuotedString)
                  lexerCSS.setColor(strC, QsciLexerCSS.DoubleQuotedString)
                  lexerCSS.setColor(QColor(cssPseudoElement), QsciLexerCSS.PseudoElement)
                  lexerCSS.setColor(QColor(cssExtendPseoudoEl), QsciLexerCSS.ExtendedPseudoElement)
                  lexerCSS.setColor(QColor(cssExtendPseoudoCl), QsciLexerCSS.ExtendedPseudoClass)
                  lexerCSS.setColor(QColor(cssPseudoCl), QsciLexerCSS.PseudoClass)
                  lexerCSS.setColor(QColor(cssPseudoCl), QsciLexerCSS.UnknownPseudoClass)
                  lexerCSS.setColor(QColor(cssVar), QsciLexerCSS.Variable)
                  lexerCSS.setColor(QColor(cssClassSelector), QsciLexerCSS.ClassSelector)
                  lexerCSS.setColor(QColor(cssIdSelector), QsciLexerCSS.IDSelector)
                  lexerCSS.setColor(QColor(cssMediaRule), QsciLexerCSS.MediaRule)
                  lexerCSS.setFont(font2, QsciLexerCSS.MediaRule)
                  lexerCSS.setColor(commentC, QsciLexerCSS.Comment)
                  lexerCSS.setFont(font2, QsciLexerCSS.Comment)
                  lexerCSS.setFont(font2, QsciLexerCSS.IDSelector)
                  self.setFont(font1)
                  lexerCSS.setFont(font1, QsciLexerCSS.Tag)
                  lexerCSS.setFoldCompact(True)
                  self.lexerCSS = lexerCSS
                  self.setCSSAutoComplete()
                  self.setCSSCallTips()
                  self.setLexer(lexerCSS)
            elif lang == "js" or lang == "javascript" or lang == "JavaScript":
                  self.style = "JavaScript"
                  self.setAutoIndent(True)
                  font2 = QFont()
                  font2.setItalic(True)
                  font2.setFamily(FontFamily.Editor)
                  font2.setPointSizeF(FontSize.FontSizeF)
                  font3 = QFont()
                  font3.setUnderline(True)
                  font3.setPointSizeF(FontSize.FontSizeF)
                  font3.setFamily(FontFamily.Editor)
                  lexerJs = LexerJS()
                  lexerJs.setDefaultFont(self.fontM)
                  lexerJs.setDefaultPaper(Theme.EditorBG)
                  lexerJs.setDefaultColor(QColor(Theme.EditorC))
                  lexerJs.setColor(Theme.EditorC, QsciLexerJavaScript.Default)
                  lexerJs.setColor(QColor(UnclosedString), QsciLexerJavaScript.UnclosedString)
                  lexerJs.setPaper(Theme.EditorBG, QsciLexerJavaScript.UnclosedString)
                  lexerJs.setFont(font3, QsciLexerJavaScript.UnclosedString)
                  lexerJs.setColor(commentC, QsciLexerJavaScript.Comment)
                  lexerJs.setPaper(Theme.EditorBG, QsciLexerJavaScript.Comment)
                  lexerJs.setFont(font2, QsciLexerJavaScript.Comment)
                  lexerJs.setColor(commentC, QsciLexerJavaScript.CommentLine)
                  lexerJs.setPaper(Theme.EditorBG, QsciLexerJavaScript.CommentLine)
                  lexerJs.setFont(font2, QsciLexerJavaScript.CommentLine)
                  lexerJs.setColor(commentC, QsciLexerJavaScript.CommentDoc)
                  lexerJs.setPaper(Theme.EditorBG, QsciLexerJavaScript.CommentDoc)
                  lexerJs.setFont(font2, QsciLexerJavaScript.CommentDoc)
                  lexerJs.setColor(QColor(Number), QsciLexerJavaScript.Number)
                  lexerJs.setPaper(Theme.EditorBG, QsciLexerJavaScript.HashQuotedString)
                  lexerJs.setColor(keyWordC, QsciLexerJavaScript.Keyword)
                  lexerJs.setFont(font2, QsciLexerJavaScript.Keyword)
                  lexerJs.setColor(keyWordC, QsciLexerJavaScript.KeywordSet2)
                  lexerJs.setFont(font2, QsciLexerJavaScript.KeywordSet2)
                  lexerJs.setColor(Theme.EditorC, QsciLexerJavaScript.Operator)
                  lexerJs.setColor(strC, QsciLexerJavaScript.SingleQuotedString)
                  lexerJs.setFont(self.fontM, QsciLexerJavaScript.SingleQuotedString)
                  lexerJs.setPaper(Theme.EditorBG, QsciLexerJavaScript.Regex)
                  lexerJs.setFont(self.fontM, QsciLexerJavaScript.Regex)
                  lexerJs.setColor(strC, QsciLexerJavaScript.DoubleQuotedString)
                  lexerJs.setFont(self.fontM, QsciLexerJavaScript.DoubleQuotedString)
                  lexerJs.setColor(strC, QsciLexerJavaScript.TripleQuotedVerbatimString)
                  lexerJs.setFont(self.fontM, QsciLexerJavaScript.TripleQuotedVerbatimString)
                  lexerJs.setColor(keyWordC, QsciLexerJavaScript.GlobalClass)
                  self.lexerJs = lexerJs
                  self.setJsAutoComplete()
                  self.setLexer(lexerJs)
            elif lang == "py" or lang == "python":
                  self.style = "Python"
                  self.setAutoIndent(True)
                  self.lexerPy = LexerPython()
                  font2 = QFont()
                  font2.setItalic(True)
                  font2.setFamily(FontFamily.Editor)
                  font2.setPointSizeF(FontSize.FontSizeF)
                  font3 = QFont()
                  font3.setUnderline(True)
                  font3.setPointSizeF(FontSize.FontSizeF)
                  font3.setFamily(FontFamily.Editor)
                  self.lexerPy.setDefaultColor(Theme.EditorC)
                  self.lexerPy.setDefaultFont(self.fontM)
                  self.lexerPy.setDefaultPaper(Theme.EditorBG)
                  self.lexerPy.setColor(Theme.EditorC, QsciLexerPython.Default)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.Default)
                  self.lexerPy.setPaper(Theme.EditorBG, QsciLexerPython.Default)
                  self.lexerPy.setColor(keyWordC, QsciLexerPython.Keyword)
                  self.lexerPy.setFont(font2, QsciLexerPython.Keyword)
                  self.lexerPy.setColor(QColor(pyClassName), QsciLexerPython.ClassName)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.ClassName)
                  self.lexerPy.setColor(Theme.EditorC, QsciLexerPython.Operator)
                  self.lexerPy.setColor(QColor(Number), QsciLexerPython.Number)
                  self.lexerPy.setColor(QColor(pyDec), QsciLexerPython.Decorator)
                  self.lexerPy.setColor(QColor(pyFunName), QsciLexerPython.FunctionMethodName)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.FunctionMethodName)
                  self.lexerPy.setColor(QColor(pyFString), QsciLexerPython.SingleQuotedFString)
                  self.lexerPy.setFont(font2, QsciLexerPython.SingleQuotedFString)
                  self.lexerPy.setColor(strC, QsciLexerPython.SingleQuotedString)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.SingleQuotedString)
                  self.lexerPy.setColor(QColor(pyFString), QsciLexerPython.DoubleQuotedFString)
                  self.lexerPy.setFont(font2, QsciLexerPython.DoubleQuotedFString)
                  self.lexerPy.setColor(strC, QsciLexerPython.DoubleQuotedString)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.DoubleQuotedString)
                  self.lexerPy.setColor(QColor(pyFString), QsciLexerPython.TripleSingleQuotedFString)
                  self.lexerPy.setFont(font2, QsciLexerPython.TripleSingleQuotedFString)
                  self.lexerPy.setColor(QColor(pyFString), QsciLexerPython.TripleDoubleQuotedFString)
                  self.lexerPy.setFont(font2, QsciLexerPython.TripleDoubleQuotedFString)
                  self.lexerPy.setColor(strC, QsciLexerPython.TripleSingleQuotedString)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.TripleSingleQuotedString)
                  self.lexerPy.setColor(strC, QsciLexerPython.TripleDoubleQuotedString)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.TripleDoubleQuotedString)
                  self.lexerPy.setPaper(Theme.EditorBG, QsciLexerPython.UnclosedString)
                  self.lexerPy.setColor(QColor(UnclosedString), QsciLexerPython.UnclosedString)
                  self.lexerPy.setFont(self.fontM, QsciLexerPython.UnclosedString)
                  self.lexerPy.setColor(QColor(Comment), QsciLexerPython.Comment)
                  self.lexerPy.setFont(font2, QsciLexerPython.Comment)
                  self.lexerPy.setColor(QColor(Comment), QsciLexerPython.CommentBlock)
                  self.lexerPy.setFont(font2, QsciLexerPython.CommentBlock)
                  self.lexerPy.setHighlightSubidentifiers(True)
                  self.setHotspotUnderline(False)
                  self.lexerPy.setAutoIndentStyle(QsciScintilla.AiClosing)
                  self.setFold()
                  self.setPythonCallTips()
                  self.setPyAutoComplete()
                  self.setLexer(self.lexerPy)
            elif lang == "json":
                  self.style = "JSON"
                  self.lexerJSON = QsciLexerJSON()
                  self.setPaper(Theme.EditorBG)
                  self.setColor(Theme.EditorC)
                  font1 = QFont()
                  font1.setPointSizeF(FontSize.FontSizeF)
                  font1.setFamily(FontFamily.Editor)
                  font1.setItalic(True)
                  self.lexerJSON.setDefaultColor(Theme.EditorC)
                  self.lexerJSON.setDefaultFont(self.fontM)
                  self.lexerJSON.setDefaultPaper(Theme.EditorBG)
                  self.lexerJSON.setColor(Theme.EditorC, QsciLexerJSON.Default)
                  self.lexerJSON.setColor(keyWordC, QsciLexerJSON.Keyword)
                  self.lexerJSON.setColor(strC, QsciLexerJSON.String)
                  self.lexerJSON.setColor(QColor(jsonIri), QsciLexerJSON.IRI)
                  self.lexerJSON.setFont(font1, QsciLexerJSON.IRI)
                  self.lexerJSON.setColor(QColor(jsonProperty), QsciLexerJSON.Property)
                  self.lexerJSON.setColor(QColor(Number), QsciLexerJSON.Number)
                  self.lexerJSON.setColor(QColor(UnclosedString), QsciLexerJSON.UnclosedString)
                  self.lexerJSON.setPaper(Theme.EditorBG, QsciLexerJSON.UnclosedString)
                  self.lexerJSON.setColor(Theme.EditorC, QsciLexerJSON.Operator)
                  self.lexerJSON.setColor(QColor(Comment), QsciLexerJSON.CommentBlock)
                  self.lexerJSON.setColor(QColor(Comment), QsciLexerJSON.CommentBlock)
                  self.lexerJSON.setColor(QColor(Comment), QsciLexerJSON.CommentLine)
                  self.lexerJSON.setColor(QColor(Comment), QsciLexerJSON.CommentLine)
                  self.setFold()
                  self.setJSONAutoComplete()
                  self.setLexer(self.lexerJSON)
            elif lang == "settings":
                  self.style = "JSON"
                  self.lexerSettings = QsciLexerJSON()
                  self.setPaper(Theme.EditorBG)
                  self.setColor(Theme.EditorC)
                  font1 = QFont()
                  font1.setPointSizeF(FontSize.FontSizeF)
                  font1.setFamily(FontFamily.Editor)
                  font1.setItalic(True)
                  self.lexerSettings.setDefaultColor(Theme.EditorC)
                  self.lexerSettings.setDefaultFont(self.fontM)
                  self.lexerSettings.setDefaultPaper(Theme.EditorBG)
                  self.lexerSettings.setColor(Theme.EditorC, QsciLexerJSON.Default)
                  self.lexerSettings.setColor(keyWordC, QsciLexerJSON.Keyword)
                  self.lexerSettings.setColor(strC, QsciLexerJSON.String)
                  self.lexerSettings.setColor(QColor(jsonIri), QsciLexerJSON.IRI)
                  self.lexerSettings.setFont(font1, QsciLexerJSON.IRI)
                  self.lexerSettings.setColor(QColor(jsonProperty), QsciLexerJSON.Property)
                  self.lexerSettings.setColor(QColor(Number), QsciLexerJSON.Number)
                  self.lexerSettings.setColor(QColor(UnclosedString), QsciLexerJSON.UnclosedString)
                  self.lexerSettings.setPaper(Theme.EditorBG, QsciLexerJSON.UnclosedString)
                  self.lexerSettings.setColor(Theme.EditorC, QsciLexerJSON.Operator)
                  self.lexerSettings.setColor(QColor(Comment), QsciLexerJSON.CommentBlock)
                  self.lexerSettings.setColor(QColor(Comment), QsciLexerJSON.CommentBlock)
                  self.lexerSettings.setColor(QColor(Comment), QsciLexerJSON.CommentLine)
                  self.lexerSettings.setColor(QColor(Comment), QsciLexerJSON.CommentLine)
                  self.setFold()
                  self.setSettingsAutoComplete()
                  self.setLexer(self.lexerSettings)
      def some_function(self, position, modifiers):
            print("Hotspot clicked at position: " + str(position))
      def setSettingsAutoComplete(self):
            self.autocomplete = QsciAPIs(self.lexerSettings)
            self.autocomplete.prepare()
            self.setAutoCompletionThreshold(AutoCompletionDelay)
            self.setAutoCompletionSource(QsciScintilla.AcsAll)
            self.setAutoCompletionCaseSensitivity(False)
            self.setAutoCompletionReplaceWord(AutoCompletionReplaceWord)
            self.setAutoCompletionShowSingle(True)
            self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)
            self.autoCompleteFromAll()
      def setJSONAutoComplete(self):
            self.autocomplete = QsciAPIs(self.lexerJSON)
            for words in Values:
                  self.autocomplete.add(words)
            if "json" in data:
                  for files in data["json"]:
                        self.autocomplete.load(f"{loc}/{files}")
            self.autocomplete.prepare()
            self.setAutoCompletionThreshold(AutoCompletionDelay)
            self.setAutoCompletionSource(QsciScintilla.AcsAll)
            self.setAutoCompletionCaseSensitivity(False)
            self.setAutoCompletionReplaceWord(AutoCompletionReplaceWord)
            self.setAutoCompletionShowSingle(True)
            self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)
            self.autoCompleteFromAll()
      def setPyAutoComplete(self):
            self.autocomplete = QsciAPIs(self.lexerPy)
            for words in Methods:
                  self.autocomplete.add(words)
            for keywords in Keywords:
                  self.autocomplete.add(keywords)
            for words in PyOthers:
                  self.autocomplete.add(words)
            for words in builtin:
                  self.autocomplete.add(words)
            if "python" in data:
                  for files in data["python"]:
                        self.autocomplete.load(f"{loc}/{files}")
            self.autocomplete.prepare()
            self.setAutoCompletionThreshold(AutoCompletionDelay)
            self.setAutoCompletionSource(QsciScintilla.AcsAll)
            self.setAutoCompletionCaseSensitivity(False)
            self.setAutoCompletionReplaceWord(AutoCompletionReplaceWord)
            self.setAutoCompletionShowSingle(True)
            self.setAutoCompletionFillupsEnabled(False)
            self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)
            self.autoCompleteFromAll()
      def setFold(self):
            x = self.FoldStyle(self.FoldStyle(QsciScintilla.FoldStyle.PlainFoldStyle)) 
            if not x:
                  self.foldAll(False)
            self.setFolding(x)
      def unsetFold(self):
            self.setFolding(0)
      def isSCharStartInAC(self, ch):
            if self.style is None:
                  return False
            wseps = self.lexerPy.autoCompletionWordSeparators()
            return any(wsep.endswith(ch) for wsep in wseps)
      def getlineAndCol(self):
            line = self.getCursorPosition()[0] + 1
            colm = self.getCursorPosition()[1] + 1
            self.parent.btn1.setText(f"Ln: {line}, Col: {colm}")
      def getSelectedCharNum(self):
            if self.hasSelectedText():
                  line = self.getCursorPosition()[0] + 1
                  colm = self.getCursorPosition()[1] + 1
                  start = self.SendScintilla(QsciScintilla.SCI_GETSELECTIONSTART)
                  end = self.SendScintilla(QsciScintilla.SCI_GETSELECTIONEND)
                  self.parent.btn1.setText(f"Ln: {line}, Col: {colm} (Selected: {end-start})")
      def undoAct(self):
            self.undo()
      def redoAct(self):
            self.redo()
      def setJsAutoComplete(self):
            self.setAutoCompletionCaseSensitivity(False)
            self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
            self.setAutoCompletionThreshold(AutoCompletionDelay)
            self.updateAutoCompleteJs()
      def setHtmlAutoComplete(self):
            self.setAutoCompletionCaseSensitivity(False)
            self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
            self.setAutoCompletionThreshold(AutoCompletionDelay)
            self.updateAutoCompleteHTM()
      def updateAutoCompleteJs(self, text=None):
            self.autocomplete = QsciAPIs(self.lexerJs)
            for words in jsKeywords:
                  self.autocomplete.add(words)
            for words in JSOthers:
                  self.autocomplete.add(words)
            if "javaScript" in data:
                  for files in data["javaScript"]:
                        self.autocomplete.load(f"{loc}/{files}")
            if not text:
                  firstList = []   
                  secondList = []  
                  for item in secondList:
                        self.autocomplete.add(item)
                  self.autocomplete.prepare()
      def updateAutoCompleteHTM(self, text=None):
            self.autocomplete = QsciAPIs(self.lexerHTML)
            self.keywords = self.lexerHTML.keywords(1)
            self.keywords = self.keywords.split(' ')
            for word in self.keywords:
                  self.autocomplete.add(word)
            for words in HTMLOtherList:
                  self.autocomplete.add(words)
            for words in HTMLOthers:
                  self.autocomplete.add(words)
            if "html" in data:
                  for files in data["html"]:
                        self.autocomplete.load(f"{loc}/{files}")
            if not text:
                  firstList = []   
                  secondList = []  
                  for item in secondList:
                        self.autocomplete.add(item)
                  self.autocomplete.prepare()
      def setCSSAutoComplete(self):
            self.setAutoCompletionCaseSensitivity(False)
            self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAPIs)
            self.setAutoCompletionThreshold(AutoCompletionDelay)
            self.updateAutoCompleteCSS()
      def updateAutoCompleteCSS(self, text=None):
            self.autocomplete = QsciAPIs(self.lexerCSS)
            for words in CSSOtherList:
                  self.autocomplete.add(words)
            for words2 in CSSOther2:
                  self.autocomplete.add(words2)
            if "css" in data:
                  for files in data["css"]:
                        self.autocomplete.load(f"{loc}/{files}")
            if not text:
                  firstList = []   
                  secondList = []
                  for item in secondList:
                        self.autocomplete.add(item)
                  self.autocomplete.prepare()
      def setPythonCallTips(self):
            self.setCallTipsStyle(QsciScintilla.CallTipsStyle.CallTipsNoContext)
            self.setCallTipsPosition(QsciScintilla.CallTipsAboveText)
            self.setCallTipsBackgroundColor(Theme.CallTipBG)
            self.setCallTipsForegroundColor(Theme.CallTipC)
            self.setCallTipsHighlightColor(Theme.HighlightedCallTip)
            self.setCallTipsVisible(CallTipsEnabled)
      def setCSSCallTips(self):
            self.setCallTipsVisible(CallTipsEnabled)
      def onSelection(self):
            if Selection.MultiCursorEditing is True:
                  return
            if self.selection_lock == False:
                  self.selection_lock = True
                  selectedText = self.selectedText()
                  self.clearSelectionHighlights()
                  if selectedText.isidentifier():
                        self.highlightSelectedText(selectedText, case_sensitive=True,regular_expression=True)
                        self.setCaretLineBackgroundColor(Editor_Dark)
                  self.selection_lock = False
      def highlightSelectedText(self, highlight_text, case_sensitive=True, regular_expression=False):
            self.setIndicator("selection")
            matches = self.findAll(
                  highlight_text,
                  case_sensitive,
                  regular_expression,
                  text_to_bytes=True,
                  whole_words=True
            )
            if matches:
                  self.highlight(matches)
      def findAll(self,search_text, case_sensitive=True, regular_expression=False, text_to_bytes=False,whole_words=False):
            matches = index_strings_in_text(
                  search_text, 
                  self.text(), 
                  case_sensitive, 
                  regular_expression, 
                  text_to_bytes,
                  whole_words
                  )
            return matches
      def highlight(self, list):
            """
            Not done by me!
            INFO:This is done using the scintilla "INDICATORS" described in the official
                scintilla API (http://www.scintilla.org/ScintillaDoc.html#Indicators)
            """
            scintilla_command = QsciScintillaBase.SCI_INDICATORFILLRANGE
            for highlight in list:
                  start   = highlight[1]
                  length  = highlight[3] - highlight[1]
                  self.SendScintilla(
                        scintilla_command, 
                        start, 
                        length
                  )
      def clearSelectionHighlights(self):
            self.clearIndicatorRange(0,0,self.lines(),self.lineLength(self.lines()-1),self.selection_indicator)
            self.setCaretLineBackgroundColor(QColor.fromRgbF(Caret.CaretBColorR,Caret.CaretBColorG,Caret.CaretBColorB, Caret.CaretBColorA))
      def setIndicatorStyle(self, indicator,color):
            self.indicatorDefine(QsciScintilla.RoundBoxIndicator, indicator)
            self.setIndicatorForegroundColor(color, indicator)
            self.SendScintilla(QsciScintillaBase.SCI_SETINDICATORCURRENT, indicator)
      def setIndicator(self, indicator):
            if indicator == "selection":
                  self.setIndicatorStyle(self.selection_indicator, Indicator.Color)
      def character_added(self, character_no):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if self.isPythonFile():
                        char = chr(character_no)
                        if char not in ['(', ')', '{', '}', '[', ']', ' ', ',', "'", '"','\n', ':']:
                              return
                        line = self.getCursorPosition()[0]
                        col = self.getCursorPosition()[1]
                        if (
                              self.isInPyComment(line, col) or
                              (char != '"' and self.isInDoubleQuotedStringPy()) or
                              (char != '"' and self.isInTripleDoubleQuotedStringPy()) or
                              (char != "'" and self.isInSingleQuotedStringPy()) or
                              (char != "'" and self.isInTripleSingleQuotedStringPy())
                        ):
                              return
                        if char == " ":
                              text = self.text(line)[:col]
                              # custom characters for FastEdit
                              if self.import_r.fullmatch(text):
                                    self.insert("import ")
                                    self.setCursorPosition(line, col + 7)            
                        elif char == "(":
                              text = self.text(line)[:col]
                              if CompleteBraces is True:
                                    if (
                                          self.def_r.fullmatch(text) is not None or
                                          self.class_r.fullmatch(text) is not None
                                    ):
                                          self.insert("):")
                                    else:
                                          self.insert(")")
                        if CompleteBraces is True:
                              if char == "{":
                                    self.insert("}")
                              elif char == "[":
                                    self.insert("]")
                              elif char == "'":
                                    self.insert("'")
                              elif char == '"':
                                    self.insert('"')
                              elif char == ',':
                                    self.insert(' ')
                                    self.setCursorPosition(line, col + 1)

                  elif self.isCSSFile():
                        if CompleteBraces is True:
                              char = chr(character_no)
                              line = self.getCursorPosition()[0]
                              col = self.getCursorPosition()[1]
                              if (
                              self.isInCSSComment(line, col) or
                              (char != '"' and self.isInDoubleQuotedStringCSS()) or
                              (char != "'" and self.isInSingleQuotedStringCSS())
                              ):
                                    return
                              if MagicTyping is True:
                                    if char == " ":
                                          text = self.text(line)[:col]
                                          for patterns in self.list_css_r:
                                                if patterns.fullmatch(text):
                                                      self.insert("{\n}")
                                                      self.setCursorPosition(line, col + 1)  
                              elif char == "(":
                                    self.insert(")")
                              elif char == "{":
                                    self.insert("}")
                              elif char == "[":
                                    self.insert("]")
                              elif char == "'":
                                    self.insert("'")
                              elif char == '"':
                                    self.insert('"')
                              elif char == ',':
                                    self.insert(' ')
                                    self.setCursorPosition(line, col + 1)
                              elif char == ":":
                                    self.insert(" ;")
                                    self.setCursorPosition(line, col + 1)
                  elif self.isJavaScriptFile():
                        if CompleteBraces is True:
                              char = chr(character_no)
                              line = self.getCursorPosition()[0]
                              col = self.getCursorPosition()[1]
                              if char == "(":
                                    self.insert(")")
                              elif char == "{":
                                    self.insert("}")
                              elif char == "[":
                                    self.insert("]")
                              elif char == "'":
                                    self.insert("'")
                              elif char == '"':
                                    self.insert('"')
                              elif char == ',':
                                    self.insert(' ')
                                    self.setCursorPosition(line, col + 1)
                  elif self.isHTMLFile():
                        if CompleteBraces is True:
                              char = chr(character_no)
                              line = self.getCursorPosition()[0]
                              col = self.getCursorPosition()[1]
                              if (
                              self.isInHTMLComment(line, col) or
                              (char != '"' and self.isInDoubleQuotedStringHTML()) or
                              (char != "'" and self.isInSingleQuotedStringHTML())
                              ):
                                    return
                              if char == " ":
                                    text = self.text(line)[:col]
                                    if self.doctype_r.fullmatch(text):
                                          self.insert("html")
                                          self.setCursorPosition(line, col + 5)
                                    if self.U_doctype_r.fullmatch(text):
                                          self.insert("html")
                                          self.setCursorPosition(line, col + 5)
                              elif char == "(":
                                    self.insert(")")
                              elif char == "{":
                                    self.insert("}")
                              elif char == "[":
                                    self.insert("]")
                              elif char == "'":
                                    self.insert("'")
                              elif char == '"':
                                    self.insert('"')
                              elif char == "<":
                                    self.insert(">")
                  elif self.isJSONFile() or self.isSettingFile():
                        if CompleteBraces is True:
                              char = chr(character_no)
                              line = self.getCursorPosition()[0]
                              col = self.getCursorPosition()[1]
                              if char == " ":
                                    text = self.text(line)[:col]
                                    if self.json_col_str_r.fullmatch(text):
                                          self.insert(" ;")
                                          self.setCursorPosition(line, col + 1)
                              elif char == "(":
                                    self.insert(")")
                              elif char == "{":
                                    self.insert("}")
                              elif char == "[":
                                    self.insert("]")
                              elif char == "'":
                                    self.insert("'")
                              elif char == '"':
                                    self.insert('"')
                              elif char == ":":
                                    self.insert(" ;")
                                    self.setCursorPosition(line, col + 1)
                  else:
                        if Typing_CompleteBraces is True:
                              char = chr(character_no)
                              line = self.getCursorPosition()[0]
                              col = self.getCursorPosition()[1]
                              if char == "(":
                                    self.insert(")")
                              elif char == "{":
                                    self.insert("}")
                              elif char == "[":
                                    self.insert("]")
                              elif char == "'":
                                    self.insert("'")
                              elif char == '"':
                                    self.insert('"')
      def isInPyComment(self, line, col):
            txt = self.text(line)
            if col == len(txt):
                  col -= 1
            while col >= 0:
                  if txt[col] == "#":
                        return True
                  col -= 1
            return False
      def isInHTMLComment(self, line, col):
            txt = self.text(line)
            if col == len(txt):
                  col -= 1
            while col >= 0:
                  if txt[col] == "<!--":
                        return True
                  col -= 1
            return False
      def isInCSSComment(self, line, col):
            txt = self.text(line)
            if col == len(txt):
                  col -= 1
            while col >= 0:
                  if txt[col] == "/*":
                        return True
                  col -= 1
            return False
      def currentBlockStyle(self, pos):
            return self.SendScintilla(QsciScintilla.SCI_GETSTYLEAT, pos)
      def currentStyle(self):
            currentPos = self.SendScintilla(QsciScintilla.SCI_GETCURRENTPOS)
            return self.currentBlockStyle(currentPos)
      def isInDoubleQuotedStringPy(self):
            return self.currentStyle() == QsciLexerPython.DoubleQuotedString
      def isInSingleQuotedStringPy(self):
            return self.currentStyle() == QsciLexerPython.SingleQuotedString
      def isInTripleDoubleQuotedStringPy(self):
            return self.currentStyle() == QsciLexerPython.TripleDoubleQuotedString
      def isInTripleSingleQuotedStringPy(self):
            return self.currentStyle() == QsciLexerPython.TripleSingleQuotedString
      def isInDoubleQuotedStringHTML(self):
            return self.currentStyle() == QsciLexerHTML.HTMLDoubleQuotedString
      def isInSingleQuotedStringHTML(self):
            return self.currentStyle() == QsciLexerHTML.HTMLSingleQuotedString
      def isInDoubleQuotedStringCSS(self):
            return self.currentStyle() == QsciLexerCSS.DoubleQuotedString
      def isInSingleQuotedStringCSS(self):
            return self.currentStyle() == QsciLexerCSS.SingleQuotedString
      def isHTMLFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".html" or file_ext == ".htm":
                        return True
      def isCSSFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".css" or file_ext == ".qss":
                        return True
      def isJavaScriptFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".js" or file_ext == ".jsx":
                        return True
      def isPythonFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".py" or file_ext == ".pyw" or file_ext == ".pyi" or file_ext == ".pyc" or file_ext == ".pyd":
                        return True
      def isJSONFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".json" or file_ext == ".jsonc":
                        return True
      def isSettingFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".fe_settings":
                        return True
      def isUIFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".ui":
                        return True
      def isJavaFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".java":
                        return True
      def isMarkDownFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".md":
                        return True
      def isCTypeFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".c" or file_ext == ".c++" or file_ext == ".h" or file_ext == ".cpp":
                        return True
      def isCSharpFile(self):
            if self.path:
                  file_ext = getFileExt(self.path)
                  if file_ext == ".cs" or file_ext == ".c#":
                        return True
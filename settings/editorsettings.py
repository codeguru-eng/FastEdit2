from sys import call_tracing, flags
from PyQt5.QtGui import QColor
from PyQt5.Qsci import *
from data.stylesheets import *
"""Note: You will need to restart app to apply settings."""

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/settings_folder/editor.fe_settings")
with open(path, "r") as file:
	_text = file.read()
data = json.loads(_text)
class Caret:
	CaretWidth          = data["Caret"]["CaretWidth"]
	CaretColor          = data["Caret"]["CaretColor"]
	if data["Caret"]["LineHighlighting"] is True:
		CaretBColorR        = data["Caret"]["LineHighlightColor"]["r"]
		CaretBColorG        = data["Caret"]["LineHighlightColor"]["g"]
		CaretBColorB        = data["Caret"]["LineHighlightColor"]["b"]
		CaretBColorA        = data["Caret"]["LineHighlightColor"]["alpha"]
	elif data["Caret"]["LineHighlighting"] is False:
		CaretBColorR        = 51
		CaretBColorG        = 51
		CaretBColorB        = 51
		CaretBColorA        = 0
	if data["Caret"]["CaretStyle"] == "line":
		CaretStyle = QsciScintilla.CARETSTYLE_LINE
	elif data["Caret"]["CaretStyle"] == "block":
		CaretStyle = QsciScintilla.CARETSTYLE_BLOCK
	elif data["Caret"]["CaretStyle"] == "overstrike-bar":
		CaretStyle = QsciScintilla.CARETSTYLE_OVERSTRIKE_BAR
	elif data["Caret"]["CaretStyle"] == "overstrike-block":
		CaretStyle = QsciScintilla.CARETSTYLE_OVERSTRIKE_BLOCK
	elif data["Caret"]["CaretStyle"] == "block-after":
		CaretStyle = QsciScintilla.CARETSTYLE_BLOCK_AFTER
	elif data["Caret"]["CaretStyle"] == "invisible":
		CaretStyle = QsciScintilla.CARETSTYLE_INVISIBLE
class Indent:
	AutoIndent          = data["Indent"]["AutoIndent"]
	BackSpaceUnIndent   = data["Indent"]["BackSpaceUnindent"]
	IndentuseTabs       = data["Indent"]["IndentUseTabs"]
class Indicator:
	Color               = QColor(data["HighlightMatchesIndicatorColor"]["r"],data["HighlightMatchesIndicatorColor"]["g"],data["HighlightMatchesIndicatorColor"]["b"],data["HighlightMatchesIndicatorColor"]["alpha"])
class Selection:
	ColorBG 		  	= QColor(data["SelectionBackgroundColor"]["r"],data["SelectionBackgroundColor"]["g"],data["SelectionBackgroundColor"]["b"],data["SelectionBackgroundColor"]["alpha"])
	if data["MultiCursorEditing"] is True:
		MultiCursorEditing = True
	elif data["MultiCursorEditing"] is False:
		MultiCursorEditing = False
if data["BraceMatching"] is True:
	BraceMatching = QsciScintilla.BraceMatch.SloppyBraceMatch
elif data["BraceMatching"] is False:
	BraceMatching = QsciScintilla.BraceMatch.NoBraceMatch
if data["LineNumbersVisible"] is True:
	LineNumbersVisible = True
elif data["LineNumbersVisible"] is False:
	LineNumbersVisible = False
if data["Suggestions"]["CallTipsEnabled"] is True:
	CallTipsEnabled = True
if data["Suggestions"]["CallTipsEnabled"] is False:
	CallTipsEnabled = False
Encoding		 				= data["Encoding"]
AutoCompletionDelay 			= data["Suggestions"]["AutoCompletionDelay"]
OverWriteMode					= data["OverWriteMode"]
AcceptDrops						= data["AcceptDrops"]
LineNumberSenstivity			= data["LineNumberSenstivity"]
AutoCompletionReplaceWord		= data["Suggestions"]["AutoCompletionReplaceWord"]
BraceMatchingBackgroundColor 	= QColor(data["BraceMatchingBackgroundColor"])
if data["Typing"]["CompleteBraces"] is True:
	CompleteBraces = True
elif data["Typing"]["CompleteBraces"] is False:
	CompleteBraces = False
if data["Typing"]["TextFile.CompleteBraces"] is True:
	Typing_CompleteBraces = True
elif data["Typing"]["TextFile.CompleteBraces"] is False:
	Typing_CompleteBraces = False
if data["Typing"]["MagicTyping"] is True:
	MagicTyping = True
elif data["Typing"]["MagicTyping"] is False:
	MagicTyping = False
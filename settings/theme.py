from data.stylesheets import *
from PyQt5.QtGui import *
import os
import json

loc = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
path = os.path.join(loc, "settings/theme.json")
with open(path, "r") as file:
      _text = file.read()
data = json.loads(_text)
class Theme:
      Window_Dark       = Dark
      Window_Light      = Light
      VScrollBar        = VScrollBar_Dark
      HScrollBar        = HScrollBar_Dark
      MenuDark          = Menu_Dark
      MenuLight         = Menu_Light
      ConsoleLabelDark  = Console_Label_Dark
      ConsoleLabelLight = Console_Label_Light
      ConsoleDarkScroll = Console_Dark_Scroll
      ConsoleLightScroll= Console_Light_Scroll
      ExplorerBarDark   = Explorer_Bar_Dark
      ExplorerBarLight  = Explorer_Bar_Light
      OutlineBarDark    = Explorer_Bar_Dark
      OutlineBarLight   = Explorer_Bar_Light
      ExplorerDark      = Explorer_Dark
      ExplorerLight     = Explorer_Light
      ExplorerLabelDark = Explorer_Label_Dark
      ExplorerLabelLight= Explorer_Label_Light
      OutlineBarLabelD = Explorer_Label_Dark
      OutlineBarLabelL = Explorer_Label_Light
      ExplorerScrollDark= Explorer_Dark_Scroll
      ExplorerScrollLight= Explorer_Light_Scroll
      ConsoleDark       = Console_Dark
      ConsoleLight      = Console_Light
      DialogButton      = Button_Dark
      TabDark           = Tab_Dark
      TabLight          = Tab_Light
      EditorBG          = Editor_Dark
      EditorC           = Editor_Color_White
      LineNumberC       = QColor("#888")
      MarginBG          = QColor(FoldArea)
      MarginC           = QColor(FoldArea)
      CallTipBG         = QColor("#444")
      CallTipC          = QColor("#ddd")
      HighlightedCallTip= QColor("lightblue")
      ConsoleTabDark    = Console_Tab_Dark
      ConsoleTabLight   = Console_Tab_Light
      OutlineDark       = Outline_Dark
      OutlineLight      = Outline_Light
if data["Theme"] == "Dark":
      ThemeC = "Dark"
elif data["Theme"] == "Light":
      ThemeC = "Light"
elif data["Theme"] == "Classic":
      ThemeC = "Classic"
else:
      ThemeC = "Dark"
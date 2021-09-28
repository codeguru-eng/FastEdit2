from settings.font import *
from settings.syntaxC import *
from PyQt5.QtGui import QColor


loc = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/"
loc = loc.replace("\\", "/")
path = os.path.join(loc, "Images/iconManager.fe_settings")
with open(path, "r") as file:
    _text = file.read()
data = json.loads(_text)

completerStyle = """
QAbstractItemView#completer
{
    background: #555;
    font-size: 18px;
    color: #ddd;
    border-radius: 5px;
    border: none;
}
QAbstractItemView#completer::item {
      background: #555;
	color: #ddd;
    border: none;
}
QAbstractItemView#completer::item:hover {
      background: #666;
	color: #ddd;
    border: none;
}
QAbstractItemView#completer::item:selected {
	background: rgb(10, 82, 190);
	color: #fff;
    border: none;

}
QAbstractItemView#completer QScrollBar {
    background: transparent;
    color: #333;
}
QAbstractItemView#completer QScrollBar:vertical {
                    border: none;
                    background: #444;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QAbstractItemView#completer QScrollBar::handle:vertical {
                    background: #555;
                    min-height: 30px;
                    border-radius: 5px;
                }
           QAbstractItemView#completer  QScrollBar::handle:vertical:hover {
                    background: #666;
                }
            QAbstractItemView#completer  QScrollBar::handle:vertical:pressed {
                    background: #777;
                }
              QAbstractItemView#completer QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #444;
                    background: #444;
                }
QAbstractItemView#completer QScrollBar {
    background: transparent;
    color: #333;
}
QAbstractItemView#completer QScrollBar:horizontal {
                    border: none;
                    background: #444;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QAbstractItemView#completer QScrollBar::handle:horizontal {
                    background: #555;
                    min-width: 30px;
                    border-radius: 5px;
                }
           QAbstractItemView#completer  QScrollBar::handle:horizontal:hover {
                    background: #666;
                }
            QAbstractItemView#completer  QScrollBar::handle:horizontal:pressed {
                    background: #777;
                }
              QAbstractItemView#completer QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    border: 2px solid #444;
                    background: #444;
                }
"""
darkThemeFile = os.path.join(loc, "data/stylesheets/DarkTheme.css")
with open(darkThemeFile, "r+") as f:
    Dark = f.read()
lightThemeFile = os.path.join(loc, "data/stylesheets/LightTheme.css")
with open(lightThemeFile, "r+") as f:
    Light = f.read()

Menu_Light = """
QMenuBar {
      background: #eee;
      color: #000;
}
QMenuBar::item
{
    background: #eee;
    padding: 5px 10px;
}
QMenuBar::item:selected
{
    background: rgb(10, 82, 190);
    color: #fff;
    border: 1px solid rgb(10, 82, 190);
}
QMenu {
      padding-top: 5px;
      padding-bottom: 5px;
	background: #eee;
	border: 1px solid #bbb;
	color: #333;
    menu-scrollable: 1;
	}
QMenu::item {
	padding: 7px 34px;
      border-radius: 2px;
	}

QMenu::item:selected{
 	background-color: rgb(10, 82, 190);
 	color: rgb(255, 255, 255);
 	}
QMenu::separator {
 	height: 2px;
      margin-top: 5px;
      margin-bottom: 5px;
 	background: #ddd;
 	}
QMenu::item:disabled {
	color: #999;
	}
QMenu::item:disabled:selected {
	background: #eee;
	}
"""
VScrollBar_Dark = """
QWidget {
     background: transparent; 
     color: #222; 
}
QScrollBar {
    background: transparent;
    color: #222;
}
QScrollBar:vertical {
                    border: none;
                    background: #222;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: #555;
                    min-height: 30px;
                    border-radius: 5px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #666;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #999;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #222;
                    background: #222;
                }
"""
HScrollBar_Dark = """
QWidget {
     background: transparent; 
     color: #222; 
}
QScrollBar:horizontal {
                    border: none;
                    background: #222;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
QScrollBar::handle:horizontal
 {
     background-color: #555;   
     min-width: 30px;
     border-radius: 5px;
 }
QScrollBar::handle:horizontal:hover {
                background: #666;
    }
                QScrollBar::handle:horizontal:pressed {
                background: #999;
        }

 QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
 {
     border: 2px solid #222;
    background: #222;
 }

"""
ScrollBar_Light = """
QScrollBar {
			width: 15px;
			border: none;
                  background: #ddd;
		}
		QScrollBar::handle {
			background: #555;
			min-height: 0px;
                  
		}
		QScrollBar::handle:hover {
			background: #666;
		}
        
"""
Menu_Dark = """
QMenuBar
{
    background-color: #333;
    color: #eee;
}
QMenuBar::item
{
    background: #333;
    padding: 5px 10px;
}
QMenuBar::item:selected
{
    background: rgb(10, 82, 190);
    border: 1px solid #3A3939;
}
QMenu {
      padding-top: 5px;
      padding-bottom: 5px;
	background: rgba(255,255,255,0.12);
	border: 1px solid #222;
	color: rgba(255,255,255,0.7);
    menu-scrollable: 1;
	}
QMenu::item {
	padding: 7px 34px;
      border-radius: 2px;
	}

QMenu::item:selected{
 	background-color: rgb(10, 82, 190);
 	color: rgb(255, 255, 255);
 	}

QMenu::separator {
 	height: 2px;
      margin-top: 7px;
      margin-bottom: 7px;
 	background: #444;
 	}
QMenu::item:disabled {
	color: #999;
	}
QMenu::item:disabled:selected {
	background: #555;
	}
"""
Button_Dark = """
QPushButton{
			border: none;
			color: #fff;
                  font-size: 17px;
                  padding: 13px 30px;
                  background: #555;
		}
		QPushButton:hover {
			background: rgb(10, 82, 190);
		}
		QPushButton:pressed {
			background: rgb(10, 82, 250);
		}
"""
Button_Light = """
QPushButton{
			border: none;
			color: #000;
                  font-size: 17px;
                  padding: 13px 30px;
                  background: #eee;
		}
		QPushButton:hover {
			background: rgb(10, 82, 190);
		}
		QPushButton:pressed {
			background: rgb(10, 82, 250);
		}
"""

Tab_Dark = f"""
QTabWidget::pane {{
   border: none;
   image: none;
}}
QTabWidget {{
   image: none;
}}
            
            QTabBar {{
                background: #333;
                image: none;
            }}
            QTabBar::close-button {{
                image: url({data["Icon"]["Tab.CloseButton"]});
                border-radius: 3px;
            }}
            QTabBar::close-button:hover {{
                background: #444;
            }}
            QTabBar::close-button:pressed {{
                background: #444;
            }}
            
            /* Style the tab using the tab sub-control. Note that
                it reads QTabBar _not_ QTabWidget */
            QTabBar::tab {{
                max-width: 200px;
                min-width: 120px;
                min-height: 30px;
                padding: 5px 10px;
                border-top: 2px solid #333;
                border-bottom: none;
                font-family: verdana;
                margin-bottom: 0px;
                color: #ccc;
                image: none;
            }}
            QTabBar::tab:hover {{
                background: rgba(0,0,0,0.2);
                border-top: 2px solid #333;
                color: #ddd;
            }}
            QTabBar::tab:selected {{
                background: #222;
                color: #fff;
            }}
            QTabBar::tab:selected {{
               border-top: 2px solid red;
               border-bottom: none;
               padding: 5px 10px;
            }}
            QTabBar::tab:unselected {{
                  border-bottom: none;
            }}
"""
Console_Tab_Dark = f"""
QTabWidget::pane {{
   border: none;
   image: none;
}}
QTabWidget {{
   image: none;
}}
            
            QTabBar {{
                background: #333;
                image: none;
            }}
            QTabBar::close-button {{
                image: url({data["Icon"]["Tab.CloseButton"]});
                border-radius: 3px;
            }}
            QTabBar::close-button:hover {{
                background: #555;
            }}
            QTabBar::close-button:pressed {{
                background: #555;
            }}
            
            /* Style the tab using the tab sub-control. Note that
                it reads QTabBar _not_ QTabWidget */
            QTabBar::tab {{
                max-width: 200px;
                min-width: 120px;
                min-height: 30px;
                padding: 5px 10px;
                border: 0px solid #fff;
                font-family: verdana;
                font-size: 18px;
                margin-bottom: 0px;
                color: rgba(255,255,255,0.5);
                border-bottom: 2px solid #333;
                image: none;
            }}
            QTabBar::tab:hover {{
                background: #333;
                color: rgba(255,255,255,0.7);
            }}

            QTabBar::tab:selected {{
               border-bottom: 2px solid #fff;
               padding: 5px 10px;
               background: #333;
               color: #fff;
            }}
"""
Console_Tab_Light = f"""
QTabWidget::pane {{
   border: none;
   image: none;
}}
QTabWidget {{
   image: none;
}}
            
            QTabBar {{
                background: #f1f1f1;
                image: none;
            }}
            
            /* Style the tab using the tab sub-control. Note that
                it reads QTabBar _not_ QTabWidget */
            QTabBar::tab {{
                max-width: 200px;
                min-width: 120px;
                min-height: 30px;
                padding: 5px 10px;
                border: 0px solid #f1f1f1;
                font-family: verdana;
                font-size: 18px;
                margin-bottom: 0px;
                color: #555;
                image: none;
                border-bottom: 2px solid #f1f1f1;
            }}
            QTabBar::tab:hover {{
                background: #f1f1f1;
                color: #333;
            }}

            QTabBar::tab:selected {{
               border-bottom: 2px solid #000;
               padding: 5px 10px;
               background: #f1f1f1;
               color: #000;
            }}
"""
Tab_Light = f"""
QTabWidget::pane {{
   border: none;
   image: none;
}}
QTabWidget {{
   image: none;
}}
QPushButton {{
    image: none;
}}
            
            QTabBar {{
                background: #555;
                image: none;
            }}
            QTabBar::close-button {{
                image: url({data["Icon"]["Tab.CloseButton"]});
                border-radius: 3px;
            }}
            QTabBar::close-button:hover {{
                background: #444;
            }}
            QTabBar::close-button:pressed {{
                background: #444;
            }}
            
            /* Style the tab using the tab sub-control. Note that
                it reads QTabBar _not_ QTabWidget */
            QTabBar::tab {{
                max-width: 200px;
                min-width: 120px;
                min-height: 30px;
                padding: 5px 10px;
                border-bottom: none;
                font-family: verdana;
                margin-bottom: 0px;
                background: #555;
                color: #ccc;
                image: none;
            }}
            QTabBar::tab:hover {{
                background: #444;
                color: #ddd;
            }}
            QTabBar::tab:selected {{
               background: #222;
                color: #fff;
               padding: 5px 10px;
            }}
"""
ToolBar_Dark = """
QToolBar {
    background: #333;
    color: #ccc;
    border: none;
}
"""
Explorer_Dark = """
QTreeView {
      show-decoration-selected: 1;
      color: #fff;
      background: #333;
      border-bottom: 2px solid #777;
    border-left: 2px solid #777;
    border-right: 2px solid #777;
          border-radius: 0px;
          padding: 5px;

  }
QTreeView:focus {
    border-left: 2px solid #888;
    border-right: 2px solid #888;
    border-bottom: 2px solid #888;
}

  QTreeView::item {
       border: none;
      border-top-color: transparent;
      border-bottom-color: transparent;
      margin: 0px;
  }

  QTreeView::item:hover {
      background: #444;
      border: none;
      color: #fff;
  }

  QTreeView::item:selected {
      border: none;
      color: #fff;
  }
  QTreeView::item:selected:active {
      border: none;
      color: #fff;
  }
  QTreeView::item:selected:!active {
      border: none;
      color: #fff;
  }
  QTreeView::branch {
  border: none;
  padding: 0;
  margin: 0;
  }
  QTreeView::branch:hover {
  border: none;
  }
  QTreeView::branch:hover {
  background: #444;
  }
  QTreeView::branch:selected:active {
  background: #444;
  }
  QTreeView::branch:selected:!active {
  background: #333;
  }
  QTreeView::branch:has-children:!has-siblings:closed,
  QTreeView::branch:closed:has-children:has-siblings {
      border-image: none;
      border: none;
      image: url(Images/Icons/iconClosed2.png);
  }
  QTreeView::branch:open:has-children:!has-siblings,
  QTreeView::branch:open:has-children:has-siblings {
      border-image: none;
      image: url(Images/Icons/iconOpened.png);
  }
  QTreeView::branch:has-children:!has-siblings:closed:hover,
  QTreeView::branch:closed:has-children:has-siblings:hover {
      background: #444;
  }
  QTreeView::branch:open:has-children:!has-siblings:hover,
  QTreeView::branch:open:has-children:has-siblings:hover {
      background: #444;
  }
 
"""
Explorer_Bar_Dark = """
border-top: 2px solid #777;
border-left: 2px solid #777;
border-right: 2px solid #777;
border-top-left-radius: 10px;
border-top-right-radius: 10px;
"""
Explorer_Bar_Light = """
border-top: 2px solid #ccc;
border-bottom: 2px solid #ccc;
border-left: 2px solid #ccc;
border-right: 2px solid #ccc;
border-top-left-radius: 10px;
border-top-right-radius: 10px;
"""
Explorer_Light = """
QTreeView {
      show-decoration-selected: 1;
      color: #000;
      background: #ebebeb;
      border-radius: 0px;
      padding: 5px;
  }
  QTreeView:focus {
      border-left: 2px solid #bbb;
    border-right: 2px solid #bbb;
    border-bottom: 2px solid #bbb;
  }

  QTreeView::item {
       border: 1px solid #ebebeb;
      border-top-color: transparent;
      border-bottom-color: transparent;
  }

  QTreeView::item:hover {
      background: #ccc;
      border: 1px solid #ebebeb;
      color: #000;
  }

  QTreeView::item:selected {
      border: 1px solid #ebebeb;
      color: #000;
  }
  QTreeView::item:selected:active {
      border: 1px solid #ebebeb;
      color: #000;
  }
  QTreeView::item:selected:!active {
      border: 1px solid #ebebeb;
      color: #000;
  }

"""
Explorer_Dark_Scroll = """
QScrollBar {
    background: transparent;
    color: #333;
}
QScrollBar:vertical {
                    border: none;
                    background: #333;
                    width: 8px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: #555;
                    min-height: 30px;
                    border-radius: 5px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #666;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #777;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #333;
                    background: #333;
                }
"""
Explorer_Light_Scroll = """
 QScrollBar:vertical {
                    border: none;
                    background: #eee;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: #ddd;
                    min-height: 0px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #ccc;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #bbb;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: #eee;
                }
                
"""
Console_Dark_Scroll = """

QScrollBar {
    background: transparent;
    color: #222;
}
QScrollBar:vertical {
                    border: none;
                    background: #333;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: #555;
                    min-height: 30px;
                    border-radius: 5px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #666;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #777;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #222;
                    background: #222;
                }
"""
Console_Light_Scroll = """
 QScrollBar:vertical {
                    border: none;
                    background: #eee;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: #ddd;
                    min-height: 0px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #ccc;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #bbb;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #eee;
                    background: #eee;
                }
 QScrollBar:horizontal {
                    border: none;
                    background: #eee;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:horizontal {
                    background: #ddd;
                    min-width: 0px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #ccc;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #bbb;
                }
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    border: 2px solid #eee;
                    background: #eee;
                }
"""
Explorer_Label_Dark = """
QLabel {
                padding-left: 0px;
                image:none;
                font-family: verdana;
                color: #ccc;
                font-size: 18px;
                background: #555;
                border-top: 2px solid #777;
                border-right: 2px solid #777;
                border-left: 2px solid #777;
           }
"""
Console_Label_Dark = """
QLabel {
                padding-left: 2px;
                image:none;
                font-family: verdana;
                color: #ccc;
                font-size: 18px;
                background: #555;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                border-top: 2px solid #777;
                border-right: 2px solid #777;
                border-left: 2px solid #777;
           }
"""
Console_Label_Light = """
QLabel {
                padding-left: 2px;
                image:none;
                font-family: verdana;
                color: #333;
                font-size: 18px;
                background: #ccc;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                border-top: 2px solid #bbb;
                border-right: 2px solid #bbb;
                border-left: 2px solid #bbb;
           }
"""
Explorer_Label_Light = """
QLabel {
                padding-left: 0px;
                image:none;
                font-family: verdana;
                color: #333;
                font-size: 18px;
                background: #ccc;
                border-top: 2px solid #bbb;
                border-right: 2px solid #bbb;
                border-left: 2px solid #bbb;
           }
"""

Console_Dark = f"""
QPlainTextEdit {{
    background: #222;
    color: #fff;
    border: none;
    selection-background-color: #333;
    border: 2px solid #777;
}}
QPlainTextEdit:focus {{
    border: 2px solid #888;
}}
"""
Console_Light = f"""
QPlainTextEdit {{
    background: #ebebeb;
    color: #000;
    border: 2px solid #ccc;
    selection-background-color: #ccc;
    selection-color: #000;
}}
QPlainTextEdit:focus {{
    border: 2px solid #bbb;
}}
"""
Outline_Dark = """
QListWidget
{
    background: #333;
    font-size: 17px;
    color: #ddd;
    border: 2px solid #777;
    border-right: 2px solid #777;
    border-radius: 0px;
    min-width: 300px;
}
QListWidget:focus {
    border: 2px solid #888;
    border-right: 2px solid #888;
}
QListWidget::item {
     border: none;
     background: #333;
}
QListWidget::item:hover {
      background: #444;
	color: #ddd;
}
QListWidget::item:selected {
	background: #555;
	color: #fff;
    border: none;
}
QListWidget QScrollBar {
    background: transparent;
    color: #333;
}
QListWidget QScrollBar:vertical {
                    border: none;
                    background: #444;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QListWidget QScrollBar::handle:vertical {
                    background: #555;
                    min-height: 30px;
                    border-radius: 5px;
                }
           QListWidget  QScrollBar::handle:vertical:hover {
                    background: #666;
                }
            QListWidget  QScrollBar::handle:vertical:pressed {
                    background: #777;
                }
              QListWidget QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #444;
                    background: #444;
                }
QListWidget QScrollBar {
    background: transparent;
    color: #333;
}
QListWidget QScrollBar:horizontal {
                    border: none;
                    background: #444;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QListWidget QScrollBar::handle:horizontal {
                    background: #555;
                    min-width: 30px;
                    border-radius: 5px;
                }
           QListWidget  QScrollBar::handle:horizontal:hover {
                    background: #666;
                }
            QListWidget  QScrollBar::handle:horizontal:pressed {
                    background: #777;
                }
              QListWidget QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    border: 2px solid #444;
                    background: #444;
                }
"""
Outline_Light = """
QListWidget
{
    background: #ebebeb;
    font-size: 17px;
    border: 2px solid #ccc;
    border-radius: 0px;
    color: #000;
    min-width: 300px;
}
QListWidget:focus {
    border: 2px solid #bbb;
}
QListWidget::item:hover {
      background: #ddd;
	color: #000;
}
QListWidget::item {
     border: none;
     background: #ebebeb;
     color: #444;
}
QListWidget::item:selected {
	background: #ccc;
    border: none;
	color: #000;
}
QListWidget QScrollBar {
    background: transparent;
    color: #ddd;
}
QListWidget QScrollBar:vertical {
                    border: none;
                    background: #ebebeb;
                    width: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QListWidget QScrollBar::handle:vertical {
                    background: #ddd;
                    min-height: 30px;
                    border-radius: 5px;
                }
           QListWidget  QScrollBar::handle:vertical:hover {
                    background: #ccc;
                }
            QListWidget  QScrollBar::handle:vertical:pressed {
                    background: #bbb;
                }
              QListWidget QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    border: 2px solid #ebebeb;
                    background: #ebebeb;
                }
QListWidget QScrollBar {
    background: transparent;
    color: #333;
}
QListWidget QScrollBar:horizontal {
                    border: none;
                    background: #444;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
            QListWidget QScrollBar::handle:horizontal {
                    background: #555;
                    min-width: 30px;
                    border-radius: 5px;
                }
           QListWidget  QScrollBar::handle:horizontal:hover {
                    background: #666;
                }
            QListWidget  QScrollBar::handle:horizontal:pressed {
                    background: #777;
                }
              QListWidget QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    border: 2px solid #444;
                    background: #444;
                }
"""

Editor_Dark  = QColor(DefaultBackground)
Editor_Light = QColor("#ddd")
Editor_Color_White = QColor(DefaultColor)

import os
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import *
from .Editor import Editor
from settings.theme import *
from settings.settings import *

class TabWidget2(QTabWidget):
      def __init__(self, parent=None):
          super(TabWidget2, self).__init__(parent)
          self.setMovable(Settings.TabMovable)
          self.setTabsClosable(True)
          self.tabCloseRequested.connect(self.remove_tab)
          self.setTabShape(QTabWidget.TabShape.Rounded)
          self.setLayoutDirection(Qt.LeftToRight)
          self.setUsesScrollButtons(Settings.TabScrollButtonsVisible)
          self.setIconSize(QtCore.QSize(Settings.TabIconWidth, Settings.TabIconHeight))
          self.setAcceptDrops(True)
          self.setMaximumWidth(800)
      def add_tab(self):
            a = self.addTab(Editor(), QIcon("Images/Icons/iconText"), "untitled")
            self.setCurrentIndex(a)
      def newTab(self, widget: QWidget, txt: str):
            self.addTab(widget, txt)
      def remove_tab(self, index):
            if self.count() == 1:
                  self.removeTab(index)
                  self.hide()
            else:
                  self.removeTab(index)
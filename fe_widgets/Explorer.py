from PyQt5 import QtCore
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import *
import sys
from settings.settings import *
from settings.theme import *
from data.fileData.folderPath import *

class Explorer(QTreeView):
      def __init__(self, parent=None):
          super().__init__(parent)
          self.folderPath = Folder_Path
          #####################
          self.fileModel = QFileSystemModel()
          self.setModel(self.fileModel)
          self.fileModel.setRootPath(QDir.rootPath())
          self.setSelectionMode(QTreeView.SingleSelection)
          self.header().setSectionResizeMode(QHeaderView.ResizeToContents)
          self.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
          self.setFrameShape(0)
          self.setUniformRowHeights(True)
          self.setAnimated(Settings.ExplorerAnimated)
          self.setIndentation(15)
          self.setHeaderHidden(True)
          self.hideColumn(1)
          self.hideColumn(2)
          self.hideColumn(3)
          self.clearSelection()
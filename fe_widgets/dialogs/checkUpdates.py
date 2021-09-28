from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import methods
import platform

appName = methods.getApplName()
writerName = methods.getWriterName()
fullAppName = methods.getFullAppName()
version = methods.getAppVersion()
appType = methods.getAppType()
Os = platform.system()
osVersion = platform.version()

class no(QMessageBox):
      def __init__(self):
            super().__init__()
            self.setWindowIcon(QIcon("Images/txteditor.png"))
            self.setWindowTitle("Check for Updates")
            reply = self.question(None, f"", \
                        f"No Updates available!", QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                  self.close()
class yes(QMessageBox):
      def __init__(self):
            super().__init__()
            self.setWindowIcon(QIcon("Images/txteditor.png"))
            self.setWindowTitle("Check for Updates")
            reply = self.question(None, f"", \
                        f"Version {version} is available. Download from github!", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                  self.close()
            else: 
                  self.close()
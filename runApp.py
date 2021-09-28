from fe_widgets.MainWindow import *
from fe_widgets.mainWidgets import *
from PyQt5.QtWidgets import QApplication
import sys
import methods

def runApp():
      """
      Execute App with QApplication.
      """
      app = QApplication(sys.argv)
      mainWindow = MainWindow()
      mainWindow.show()
      app.exec_()
if __name__ == "__main__":
      # Check if requirements are available in PC
      if methods.requirementsSatisfied() is True:
            try:
                  runApp()
            except Exception as e:
                  print(str(e))
      else:
            print("Requirements not Satisfied!")
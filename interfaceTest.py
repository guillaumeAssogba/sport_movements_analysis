import sys
from PyQt4 import QtGui
import interfaceTestQt
import test

class ExampleApp(QtGui.QMainWindow, interfaceTestQt.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        
        #File loading
        self.perfName = ""
        self.bodyName = ""
        self.pushButton.clicked.connect(self.openBodyFile)
        self.pushButton_2.clicked.connect(self.openPerfFile)
        
        #launch data processing
        self.pushButton_3.clicked.connect(self.launchAnalysis)
        
    def openBodyFile(self):
        self.bodyName = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.textBrowser.setHtml(self.bodyName)
        self.launchProcess()
        
    def openPerfFile(self):
        self.perfName = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.textBrowser_2.setHtml(self.perfName)
        self.launchProcess()
    
    def launchProcess(self):
        if self.bodyName and self.perfName:
            self.pushButton_3.setEnabled(True)
            
    def launchAnalysis(self):
        test.launchProcess2(self.bodyName, self.perfName)
            
    
          
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


        
if __name__ == '__main__':
    main()
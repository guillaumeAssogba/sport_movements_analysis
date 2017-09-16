import sys
import os
from PyQt4 import QtGui
import interface
import launchAlgo

class ExampleApp(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        
        #File loading
        self.perfName = ""
        self.bodyName = ""
        self.pushButton.clicked.connect(self.openBodyFile)
        self.pushButton_2.clicked.connect(self.openPerfFile)
        
        #group methods by default K-means
        self.groupMethod = True
        self.radioButton.toggled.connect(self.groupRandom)
        self.radioButton_2.toggled.connect(self.groupKmeans)
        
        #algo variables
        self.algorithm = [False, False, False, False, False, False]
        self.checkBox_6.clicked.connect(self.algoLoadings)
        self.checkBox_7.clicked.connect(self.algoRepresentation)
        self.checkBox_8.clicked.connect(self.algoBestWorstProjection)
        self.checkBox_5.clicked.connect(self.algoStdDeviation)
        
        #launch data processing
        self.pushButton_3.clicked.connect(self.launchAnalysis)
        
    def openBodyFile(self):
        self.bodyName = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.textBrowser.setHtml(os.path.basename(self.bodyName))
        self.launchProcess()
        
    def openPerfFile(self):
        self.perfName = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.textBrowser_2.setHtml(os.path.basename(self.perfName))
        self.launchProcess()
        
    def groupKmeans(self):
        self.groupMethod = True
        
    def groupRandom(self):
        self.groupMethod = False
        
    def algoLoadings(self):
        self.algorithm[0] = not self.algorithm[0]
        
    def algoRepresentation(self):
        self.algorithm[1] = not self.algorithm[1]
        
    def algoBestWorstProjection(self):
        self.algorithm[2] = not self.algorithm[2]
        
    def algoStdDeviation(self):
        self.algorithm[3] = not self.algorithm[3]
    
    def launchProcess(self):
        if self.bodyName and self.perfName:
            self.pushButton_3.setEnabled(True)
            
    def launchAnalysis(self):
        launchAlgo.launchProcess2(self.bodyName, self.perfName, self.groupMethod, self.algorithm, int(self.spinBox.value()))
            
    
          
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


        
if __name__ == '__main__':
    main()
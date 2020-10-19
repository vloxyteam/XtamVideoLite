from PyQt5 import QtCore, QtGui, QtWidgets

from ui_main import Ui_wMain
from video import wVideo
from empty import wEmpty
import csv
import math
import os
import subprocess

cmd = "date"
    

class wMain(QtWidgets.QMainWindow, Ui_wMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initVars() # initialize variables
        self.initUI() # initialize user interface
        
        # returns output as byte string
    returned_output = subprocess.check_output(cmd)

    # using decode() function to convert byte string to string
    print('El día de hoy es:', returned_output.decode("utf-8"))

    #########################################################################################################
    # role : initialize ui
    # param : none
    # return : none
    #########################################################################################################
    
    
    
    def initUI(self):
        # barra de herramientas
        self.tbCamera = self.addToolBar('Camera')
        self.tbCamera.setIconSize(QtCore.QSize(32, 32));
        self.tbCamera.setStyleSheet(""" background : black;
                                    color : white;
                                    border-top-style: outset;
                                    border-top-width: 1px;
                                    border-top-color: #222222;""")

        # Cargar Icono csv en la barra de tareas
        self.actLoadCSV = QtWidgets.QAction(QtGui.QIcon('img/loadcsv.png'), '&Cargar CSV ó Ctrl+L', self)
        self.actLoadCSV.setShortcut('Ctrl+L')
        self.actLoadCSV.setStatusTip('Cargar CSV')
        self.actLoadCSV.triggered.connect(self.on_act_LoadCSV)
        self.tbCamera.addAction(self.actLoadCSV)
        
        # Cargar Icono Emision 1 
        self.actEmitir1 = QtWidgets.QAction(QtGui.QIcon('img/transmision1.png'), '&Emitir ó Ctrl+1', self)
        self.actEmitir1.setShortcut('Ctrl+1')
        self.actEmitir1.setStatusTip('Empezar Streaming Cámara 1')
        self.actEmitir1.triggered.connect(self.on_act_Emitir1)
        self.tbCamera.addAction(self.actEmitir1)
        
        # Cargar espacio 
        self.actEmitir1 = QtWidgets.QAction(QtGui.QIcon(''), '|', self)
        self.actEmitir1.triggered.connect(self.on_act_Emitir1)
        self.tbCamera.addAction(self.actEmitir1)
        
        # Cargar Icono Emision 2 
        self.actEmitir2 = QtWidgets.QAction(QtGui.QIcon('img/transmision2.png'), '&Emitir ó Ctrl+2', self)
        self.actEmitir2.setShortcut('Ctrl+2')
        self.actEmitir2.setStatusTip('Empezar Streaming Cámara 2')
        self.actEmitir2.triggered.connect(self.on_act_Emitir2)
        self.tbCamera.addAction(self.actEmitir2)
        
        # Cargar espacio 2
        self.actEmitir1 = QtWidgets.QAction(QtGui.QIcon(''), '|', self)
        self.actEmitir1.setShortcut('')
        self.actEmitir1.setStatusTip('')
        self.actEmitir1.triggered.connect(self.on_act_Emitir1)
        self.tbCamera.addAction(self.actEmitir1)
        
        # Cargar Icono Emision 3 
        self.actEmitir3 = QtWidgets.QAction(QtGui.QIcon('img/transmision3.png'), '&Emitir ó Ctrl+3', self)
        self.actEmitir3.setShortcut('Ctrl+3')
        self.actEmitir3.setStatusTip('Empezar Streaming Cámara 3')
        self.actEmitir3.triggered.connect(self.on_act_Emitir3)
        self.tbCamera.addAction(self.actEmitir3)
        
        # Cargar espacio 3
        self.actEmitir1 = QtWidgets.QAction(QtGui.QIcon(''), '|', self)
        self.actEmitir1.setShortcut('')
        self.actEmitir1.setStatusTip('')
        self.actEmitir1.triggered.connect(self.on_act_Emitir1)
        self.tbCamera.addAction(self.actEmitir1)
        
        # Cargar Icono Emision 4 
        self.actEmitir4 = QtWidgets.QAction(QtGui.QIcon('img/transmision4.png'), '&Emitir ó Ctrl+4', self)
        self.actEmitir4.setShortcut('Ctrl+4')
        self.actEmitir4.setStatusTip('Empezar Streaming Cámara 4')
        self.actEmitir4.triggered.connect(self.on_act_Emitir4)
        self.tbCamera.addAction(self.actEmitir4)
        
        # Cargar espacio 4
        self.actEmitir1 = QtWidgets.QAction(QtGui.QIcon(''), '|', self)
        self.actEmitir1.setShortcut('')
        self.actEmitir1.setStatusTip('')
        self.actEmitir1.triggered.connect(self.on_act_Emitir1)
        self.tbCamera.addAction(self.actEmitir1)
        
        # Salir
        self.actSalir = QtWidgets.QAction(QtGui.QIcon('img/salir.png'), '&Salir ó Ctrl+O', self)
        self.actSalir.setShortcut('Ctrl+O')
        self.actSalir.setStatusTip('Salir')
        self.actSalir.triggered.connect(self.on_act_Salir)
        self.tbCamera.addAction(self.actSalir)
                       
        # Cargar espacio 5
        self.actEmitir1 = QtWidgets.QAction(QtGui.QIcon(''), '|', self)
        self.actEmitir1.setShortcut('')
        self.actEmitir1.setStatusTip('')
        self.actEmitir1.triggered.connect(self.on_act_Emitir1)
        self.tbCamera.addAction(self.actEmitir1)

    #########################################################################################################
    # role : initialize variables
    # param : none
    # return : none
    #########################################################################################################
    def initVars(self):
        self.arrayVideo = []  ## array of wVideo widgets
        self.arrayEmpty = []  ## array of wEmpty widgets
        self.arrayUrl = []  ## array of Url
        self.arrayAlias = []  ## array of Alias

    #########################################################################################################
    # role : load csv file included rtsp urls & alias
    # param : none
    # return : none
    #########################################################################################################
    def on_act_LoadCSV(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load CSV", "./",
                                                            "RTSP URL CSV (*.csv)", options=options)

        print("Abrir Stream - " + fileName)

        if fileName == None or not fileName:
            return

        # remove previous wVideo widgets
        for i in reversed(range(self.loGrid.count())):
            self.loGrid.itemAt(i).widget().setParent(None)

        # stop, delete all wVideo
        if self.arrayVideo:
            for wVideoItem in self.arrayVideo:
                wVideoItem.stop() # stop playing in wVideo
                del wVideoItem # delete wVideo

        # delete all wEmpty
        if self.arrayEmpty:
            for wEmptyItem in self.arrayEmpty:
                del wEmptyItem

        # clear previous csv url & alias
        self.arrayVideo = []
        self.arrayEmpty = []
        self.arrayUrl = []
        self.arrayAlias = []

        # load new csv file
        self.count = 0
        with open(fileName) as csvUrl:
            csvReader = csv.reader(csvUrl, delimiter=',')
            for row in csvReader:
                self.count += 1
                self.arrayUrl.append(row[0].strip()) # store new url
                self.arrayAlias.append(row[1].strip()) # stor new alias

        print("Conteo total - " + str(self.count))

        # calculate rows & cols of grid
        self.rows, self.cols = self.arrange(self.count)

        index = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if index < self.count:
                    # create new wVidoe
                    wVideoItem = wVideo(self.arrayUrl[index], self.arrayAlias[index])
                    self.arrayVideo.append(wVideoItem)
                    self.loGrid.addWidget(wVideoItem, row, col)
                else:
                    # create new empty area
                    wEmptyItem = wEmpty()
                    self.loGrid.addWidget(wEmptyItem, row, col)

                index += 1
                
    #########################################################################################################
    # role : Emitir1
    # param : none
    # return : none
    #########################################################################################################
    def on_act_Emitir1(self):
        
        os.system("sh ./scripts/rtsp-rtmp.sh")
        print ("Emitiendo 1...")
        
    
    #########################################################################################################
    # role : Emitir2
    # param : none
    # return : none
    #########################################################################################################
    def on_act_Emitir2(self):
        
        os.system("sh ./scripts/rtsp-rtmp2.sh")
        print ("Emitiendo 2...")
        
        
    #########################################################################################################
    # role : Emitir3
    # param : none
    # return : none
    #########################################################################################################
    def on_act_Emitir3(self):
        
        os.system("sh ./scripts/rtsp-rtmp.sh")
        print ("Emitiendo 3...")    
    
    
    #########################################################################################################
    # role : Emitir4
    # param : none
    # return : none
    #########################################################################################################
    def on_act_Emitir4(self):
        
        os.system("sh ./scripts/rtsp-rtmp2.sh")
        print ("Emitiendo 4...") 
        
                
    #########################################################################################################
    # role : Detener Emitir
    # param : none
    # return : none
    #########################################################################################################
    def on_act_Detener(self):
        
         os.system("killall ffmpeg")
         os.system("killall python")
         print ("Deteniendo...")
        
     #########################################################################################################
    # role : Salir
    # param : none
    # return : none
    #########################################################################################################
    def on_act_Salir(self):
        

        
        os.system("sudo pkill ffmpeg / sudo pkill python3")
        print("Muerto Ffmpeg ")
        os.system("ffmpeg")
        os.system("pkill python3")
        print("Muerto python3")
        print(os.name)
        if self.arrayVideo:
            for wVideoItem in self.arrayVideo:
                ## stop, delete wVideo
                wVideoItem.stop()
                del wVideoItem


    #########################################################################################################
    # role : main window close event
    # param : close event
    # return : none
    #########################################################################################################
    def closeEvent(self, *args, **kwargs):
        # stop, delete all wVideo
        if self.arrayVideo:
            for wVideoItem in self.arrayVideo:
                ## stop, delete wVideo
                wVideoItem.stop()
                del wVideoItem

    #########################################################################################################
    # role : calculate rows and cols of gridlayout from total rtsp count
    # param : total rtsp count
    # return : rows, cols
    #########################################################################################################
    def arrange(self, count):
        rows = math.sqrt(count)
        cols = rows
        if rows != int(rows):
            rows = round(rows, 0)
            cols += 1

        rows = int(rows)
        cols = int(cols)

        return rows, cols

#########################################################################################################
# role : entry point
#########################################################################################################
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    wMain = wMain()
    wMain.show()
    sys.exit(app.exec_())


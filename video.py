from PyQt5 import QtCore, QtGui, QtWidgets

from ui_video import Ui_wVideo
import threading
import sys
import vlc
import datetime
import time


class wVideo(QtWidgets.QWidget, Ui_wVideo):
    def __init__(self, url, alias):
        super().__init__()
        self.setupUi(self)

        ## variables de inicio
        self.url = url # URL de transmisión rtsp
        self.alias = alias # alias a la URL del flujo rtsp

        self.procFFMpeg = None # proceso a ffmpeg para grabar
        self.fileName = "" # nombre de archivo grabado de ffmpeg
        self.bConnectedAlertShown = False # comprobar el estado de alerta cuando rtsp se vuelve a conectar

        # inicializar la interfaz de usuario
        self.initUI()

        ## comenzar a transmitir
        self.openStreaming()

        ## hilo de inicio para monitorear el estado desconectado
        self.bStopThread = False
        self.thread = threading.Thread(target=self.thread_loop)
        self.thread.start()

    #########################################################################################################
    # rol: inicializar ui
    # param: none
    # retorno: ninguno
    #########################################################################################################
    
    def initUI(self):
        # establecer imágenes en el botón de reproducción y pausa
        self.btnResume.setPixmap(
            QtGui.QPixmap("img/resume_normal.png"),
            QtGui.QPixmap("img/resume_normal_hover.png"),
            QtGui.QPixmap("img/resume_pressed.png"),
            QtGui.QPixmap("img/resume_pressed_hover.png"))
        self.btnResume.setCheckable(True) # configurar el modo de botón para alternar

        # establecer imágenes en el botón de grabación
        self.btnRecord.setPixmap(
            QtGui.QPixmap("img/record_normal.png"),
            QtGui.QPixmap("img/record_normal_hover.png"),
            QtGui.QPixmap("img/record_pressed.png"),
            QtGui.QPixmap("img/record_pressed_hover.png"))
        self.btnRecord.setCheckable(True)# configurar el modo de botón para alternar

        self.lblAlias.setText(self.alias) # mostrar alias en video

        # creando una instancia básica de vlc
        self.instance = vlc.Instance()
        # creando un reproductor multimedia vlc vacío
        self.mediaplayer = self.instance.media_player_new()

        if sys.platform.startswith('linux'):  # para Linux usando el X server
            self.mediaplayer.set_xwindow(self.frmVideo.winId())
        elif sys.platform == "win32":  # para ventanas
            self.mediaplayer.set_hwnd(self.frmVideo.winId())

        self.isPaused = False

        ## conectar señal / ranura
        self.btnResume.toggled.connect(self.on_btn_Resume)
        self.btnRecord.toggled.connect(self.on_btn_Record)

    #########################################################################################################
    # rol: alternar abrir y pausar
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def toggleResume(self):
        """Cambiar el estado de reproducción / pausa
        """
        if self.mediaplayer.is_playing():
            # pausar la transmisión
            self.mediaplayer.pause()
            self.isPaused = True
            self.btnResume.setChecked(True)
        else:
            # reanudar la reproducción
            if self.mediaplayer.play() == -1:
                self.isPaused = True
                self.btnResume.setChecked(False)
                return

            self.isPaused = False
            self.btnResume.setChecked(False)

    #########################################################################################################
    # papel: dejar de reproducir la transmisión
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def stop(self):
        # detener hilo
        self.bStopThread = True
        while self.thread.isAlive():
            time.sleep(0.01)

        # dejar de reproducir
        self.mediaplayer.stop()
        while self.mediaplayer.is_playing():
            time.sleep(0.01)

        print("detenido - " + self.alias)

    #########################################################################################################
    # rol: abrir transmisión 
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def openStreaming(self):
        self.mediaplayer.set_mrl(self.url, "network-caching=300") # establecer URL
        self.mediaplayer.video_set_mouse_input(True) # mostrar el mouse en el marco
        self.mediaplayer.video_set_key_input(False) # evento de teclado prohibido
        self.mediaplayer.audio_set_mute(True)  # silenciar el audio

        # Abrir reproduccion de la transmisión
        self.toggleResume()

    #########################################################################################################
    # función: alternar reproducción de transmisión y pausa
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def on_btn_Resume(self):
        self.toggleResume() # reproducir y pausar

    #########################################################################################################
    # función: comprobar el estado desconectado de Internet y la transmisión
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def isAccident(self):
        # cuando el evento de pausa no se produjo manualmente y el jugador no está jugando
        if self.isPaused == False and self.mediaplayer.is_playing() == False:
            return True
        return False

    #########################################################################################################
    # rol: botón alternar evento del botón de grabación
    # param: bRecord: alternar estado
    # Verdadero: comienza a grabar
    # Falso: detener la grabación
    # retorno: ninguno
    #########################################################################################################
    def on_btn_Record(self, bRecord):
        if self.isAccident():
            self.btnRecord.setChecked(False)
            print("la grabación falló debido a un accidente - " + self.alias)

        if bRecord == True:
            ## inicio de registro
            # nombre de archivo a grabar
            self.fileName = self.alias + datetime.datetime.now().strftime("_%Y%m%d%H%M%S.mp4")

            # proceso para ffmpeg
            self.procFFMpeg = QtCore.QProcess()
            self.procFFMpeg.setStandardInputFile(self.procFFMpeg.nullDevice())
            self.procFFMpeg.setStandardOutputFile(self.procFFMpeg.nullDevice())
            self.procFFMpeg.setStandardErrorFile(self.procFFMpeg.nullDevice())

            
            # evento finalizado del proceso ffmpeg
            self.procFFMpeg.finished.connect(self.on_Record_Finished)

            program = "ffmpeg"
            args = ["-i", self.url, "-vcodec", "copy", "-strict", "-2", "-y", self.fileName]

            self.procFFMpeg.setProgram(program)
            self.procFFMpeg.setArguments(args)
            self.procFFMpeg.start()
            self.procFFMpeg.waitForStarted(10000)

            print("started recording - " + self.fileName)
        else:
            # para de grabar
            self.procFFMpeg.terminate()
            if not self.procFFMpeg.waitForFinished(10000):
                self.procFFMpeg.kill()

    #########################################################################################################
    # rol: grabación del evento terminado del proceso ffmpeg
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def on_Record_Finished(self):
        self.btnRecord.setChecked(False)
        print("stopped recording - " + self.fileName)

    #########################################################################################################
    # rol: ciclo de bucle del hilo que monitorea el estado desconectado
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def thread_loop(self):
        # comprobar estado desconectado
        while True:
            if self.isAccident():
                self.on_Accident()
                self.bConnectedAlertShown = False
            else:
                if self.bConnectedAlertShown == False:
                    print("connected - " + self.alias)

                self.bConnectedAlertShown = True

            if self.bStopThread == True:
                break

            time.sleep(2)

    #########################################################################################################
    # rol: evento ocurrido en estado desconectado
    # param: none
    # retorno: ninguno
    #########################################################################################################
    def on_Accident(self):
        print("intentando conectar - " + self.alias)
        # abrir transmisión
        self.openStreaming()
        self.btnResume.setChecked(False)
        self.btnRecord.setChecked(False)

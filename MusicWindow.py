import ntpath
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog
from MusicGUI import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtCore import QUrl,QTime
from PySide6.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.state=False
        self.muted=True
        self.ui.button_play.setEnabled(False)

        self.player=QMediaPlayer()
        self.audio=QAudioOutput()

        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.ui.slider_volume.value()
                             )

        self.ui.button_add_file.clicked.connect(self.open_music)
        self.ui.button_play.clicked.connect(self.play_music)
        self.ui.slider_volume.sliderMoved.connect(self.volume_slider_changed)
        self.ui.slider_music.sliderMoved.connect(self.player_slider_changed)
        self.ui.button_mute1.clicked.connect(self.volume_mute)

        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
    def open_music(self):
        fileName,_=QFileDialog.getOpenFileName(self,"ADD FILE")
        if fileName !='':
            self.player.setSource(QUrl.fromLocalFile(fileName))
            self.ui.button_play.setEnabled(True)
            song=ntpath.basename(fileName)
            self.ui.NowPlaying.setText(song[0:len(song)-4])
    def play_music(self):
        if self.state==False:
            self.player.play()
            self.state=True
            self.ui.button_play.setIcon(QIcon("feather/pause-circle.svg"))
        else:
            self.player.pause()
            self.state=False
            self.ui.button_play.setIcon(QIcon("feather/play-circle.svg"))

    def position_changed(self,position):
        if (self.ui.slider_music.maximum() !=self.player.duration()):
            self.ui.slider_music.setMaximum(self.player.duration())
        self.ui.slider_music.setValue(position)

        seconds_pass=(position/1000)%60
        minutes_pass=(position/60000)%60
        hours_pass=(position/2600000)%24
        seconds_remain=((self.player.duration()-position)/1000)%60
        minutes_remain=((self.player.duration()-position)/60000)%60
        hours_remain = ((self.player.duration()-position) / 2600000) % 24
        time_pass=QTime(hours_pass,minutes_pass,seconds_pass)
        time_remain=QTime(hours_remain,minutes_remain,seconds_remain)
        self.ui.timepassed.setText(time_pass.toString())
        self.ui.timeRemain.setText(time_remain.toString())
    def duration_changed(self,duration):
        self.ui.slider_music.setRange(0,duration)

    def volume_slider_changed(self,position):
        self.ui.slider_volume.setValue(position)
        self.audio.setVolume(self.ui.slider_volume.value())

    def player_slider_changed(self,position):
        self.player.setPosition(position)
    def volume_mute(self):
        if (self.muted):
            self.audio.setMuted(True)
            self.ui.slider_volume.setValue(0)
            self.ui.button_mute1.setIcon(QIcon("feather/volume-x.svg"))
            self.muted=False
        else:
            self.audio.setMuted(False)
            self.ui.slider_volume.setValue(self.audio.volume())
            print(self.ui.slider_volume.value())
            self.ui.button_mute1.setIcon(QIcon("feather/volume-1.svg"))
            self.muted=True

app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())
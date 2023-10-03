# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1271, 841)
        MainWindow.setStyleSheet(u"background-color:rgb(93,42,66);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top = QWidget(self.centralwidget)
        self.top.setObjectName(u"top")
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QWidget(self.top)
        self.menu.setObjectName(u"menu")
        self.menu.setMaximumSize(QSize(270, 16777215))
        self.menu.setStyleSheet(u"background-color:rgb(242,156,163);")
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.tim_kiem = QWidget(self.menu)
        self.tim_kiem.setObjectName(u"tim_kiem")
        self.tim_kiem.setMaximumSize(QSize(16777215, 50))
        self.tim_kiem.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.tim_kiem)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Searcher = QLineEdit(self.tim_kiem)
        self.Searcher.setObjectName(u"Searcher")
        self.Searcher.setMinimumSize(QSize(0, 30))
        self.Searcher.setStyleSheet(u"QLineEdit{\n"
"	border: 2px soild rgb(170, 0, 255);\n"
"	border-radius: 10px;\n"
"	color:rgb(255, 255, 255);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgba(0, 0, 0, 70);\n"
"}")
        self.Searcher.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.Searcher)

        self.nut_enter = QPushButton(self.tim_kiem)
        self.nut_enter.setObjectName(u"nut_enter")
        self.nut_enter.setMinimumSize(QSize(30, 30))
        self.nut_enter.setMaximumSize(QSize(30, 30))
        self.nut_enter.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	border-radius: 7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(0, 0, 0,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/feather/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nut_enter.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.nut_enter)


        self.verticalLayout_2.addWidget(self.tim_kiem)

        self.cac_nut_bam = QWidget(self.menu)
        self.cac_nut_bam.setObjectName(u"cac_nut_bam")
        self.verticalLayout_3 = QVBoxLayout(self.cac_nut_bam)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttonMyMusic = QPushButton(self.cac_nut_bam)
        self.buttonMyMusic.setObjectName(u"buttonMyMusic")
        self.buttonMyMusic.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"OCR A Extended"])
        font.setPointSize(20)
        font.setBold(True)
        self.buttonMyMusic.setFont(font)
        self.buttonMyMusic.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(112,194,180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(75, 130, 120);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(54, 94, 87);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#ff0000;\n"
"}")
        self.buttonMyMusic.setCheckable(False)
        self.buttonMyMusic.setChecked(False)

        self.verticalLayout_3.addWidget(self.buttonMyMusic)

        self.buttonPlaylist = QPushButton(self.cac_nut_bam)
        self.buttonPlaylist.setObjectName(u"buttonPlaylist")
        self.buttonPlaylist.setMinimumSize(QSize(0, 50))
        self.buttonPlaylist.setFont(font)
        self.buttonPlaylist.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(112,194,180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(75, 130, 120);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(54, 94, 87);\n"
"}")

        self.verticalLayout_3.addWidget(self.buttonPlaylist)

        self.button_Daily_suggest = QPushButton(self.cac_nut_bam)
        self.button_Daily_suggest.setObjectName(u"button_Daily_suggest")
        self.button_Daily_suggest.setMinimumSize(QSize(0, 50))
        self.button_Daily_suggest.setFont(font)
        self.button_Daily_suggest.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(112,194,180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(75, 130, 120);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(54, 94, 87);\n"
"}")

        self.verticalLayout_3.addWidget(self.button_Daily_suggest)


        self.verticalLayout_2.addWidget(self.cac_nut_bam, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.menu)

        self.cac_page = QWidget(self.top)
        self.cac_page.setObjectName(u"cac_page")
        self.cac_page.setMinimumSize(QSize(600, 600))
        self.verticalLayout_6 = QVBoxLayout(self.cac_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.cac_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 200))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.box_tab_hien_thoi = QWidget(self.widget)
        self.box_tab_hien_thoi.setObjectName(u"box_tab_hien_thoi")
        self.box_tab_hien_thoi.setMinimumSize(QSize(0, 60))
        self.box_tab_hien_thoi.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_8 = QVBoxLayout(self.box_tab_hien_thoi)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tab_hien_thoi = QWidget(self.box_tab_hien_thoi)
        self.tab_hien_thoi.setObjectName(u"tab_hien_thoi")
        self.tab_hien_thoi.setMinimumSize(QSize(250, 50))
        self.tab_hien_thoi.setMaximumSize(QSize(250, 50))
        self.tab_hien_thoi.setStyleSheet(u"background-color:rgb(112,194,180);\n"
"border-radius: 10px;")
        self.verticalLayout_9 = QVBoxLayout(self.tab_hien_thoi)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.tab_hien_thoi)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"OCR A Extended"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)


        self.verticalLayout_8.addWidget(self.tab_hien_thoi, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.box_tab_hien_thoi, 0, Qt.AlignLeft)

        self.change_file = QWidget(self.widget)
        self.change_file.setObjectName(u"change_file")
        self.change_file.setMinimumSize(QSize(0, 60))
        self.change_file.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.change_file)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_add_file = QPushButton(self.change_file)
        self.button_add_file.setObjectName(u"button_add_file")
        self.button_add_file.setMinimumSize(QSize(170, 50))
        self.button_add_file.setMaximumSize(QSize(170, 50))
        self.button_add_file.setFont(font1)
        self.button_add_file.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(112,194,180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(75, 130, 120);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(54, 94, 87);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/feather/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_file.setIcon(icon1)
        self.button_add_file.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.button_add_file)

        self.button_Add_Folder = QPushButton(self.change_file)
        self.button_Add_Folder.setObjectName(u"button_Add_Folder")
        self.button_Add_Folder.setMinimumSize(QSize(200, 50))
        self.button_Add_Folder.setMaximumSize(QSize(200, 50))
        self.button_Add_Folder.setFont(font1)
        self.button_Add_Folder.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(112,194,180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(75, 130, 120);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(54, 94, 87);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/feather/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_Add_Folder.setIcon(icon2)
        self.button_Add_Folder.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.button_Add_Folder)

        self.button_Delete = QPushButton(self.change_file)
        self.button_Delete.setObjectName(u"button_Delete")
        self.button_Delete.setMinimumSize(QSize(170, 50))
        self.button_Delete.setMaximumSize(QSize(170, 50))
        self.button_Delete.setFont(font1)
        self.button_Delete.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(112,194,180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(75, 130, 120);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(54, 94, 87);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/feather/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_Delete.setIcon(icon3)
        self.button_Delete.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.button_Delete)


        self.verticalLayout_7.addWidget(self.change_file)


        self.verticalLayout_6.addWidget(self.widget)

        self.songList = QTableWidget(self.cac_page)
        self.songList.setObjectName(u"songList")
        self.songList.setStyleSheet(u"border: null;")

        self.verticalLayout_6.addWidget(self.songList)


        self.horizontalLayout.addWidget(self.cac_page)


        self.verticalLayout.addWidget(self.top)

        self.bot = QWidget(self.centralwidget)
        self.bot.setObjectName(u"bot")
        self.bot.setMinimumSize(QSize(0, 120))
        self.bot.setMaximumSize(QSize(16777215, 120))
        self.bot.setStyleSheet(u"background-color: rgb(247,202,205);")
        self.verticalLayout_4 = QVBoxLayout(self.bot)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bar_and_time = QWidget(self.bot)
        self.bar_and_time.setObjectName(u"bar_and_time")
        self.bar_and_time.setMinimumSize(QSize(0, 50))
        self.bar_and_time.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.bar_and_time)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.timepassed = QLabel(self.bar_and_time)
        self.timepassed.setObjectName(u"timepassed")
        self.timepassed.setMinimumSize(QSize(50, 30))
        self.timepassed.setMaximumSize(QSize(50, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.timepassed.setFont(font2)

        self.horizontalLayout_4.addWidget(self.timepassed, 0, Qt.AlignLeft)

        self.slider_music = QSlider(self.bar_and_time)
        self.slider_music.setObjectName(u"slider_music")
        self.slider_music.setMinimumSize(QSize(0, 30))
        self.slider_music.setMaximumSize(QSize(16777215, 30))
        self.slider_music.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 7px;\n"
"    background: #C0C0C0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:rgb(202, 132, 81);\n"
"    border: none;\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}")
        self.slider_music.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.slider_music)

        self.timeRemain = QLabel(self.bar_and_time)
        self.timeRemain.setObjectName(u"timeRemain")
        self.timeRemain.setMinimumSize(QSize(50, 30))
        self.timeRemain.setMaximumSize(QSize(50, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.timeRemain.setFont(font3)
        self.timeRemain.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.timeRemain, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.bar_and_time)

        self.bottom = QWidget(self.bot)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 70))
        self.bottom.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.bottom)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 10)
        self.dang_nghe = QWidget(self.bottom)
        self.dang_nghe.setObjectName(u"dang_nghe")
        self.dang_nghe.setMinimumSize(QSize(250, 0))
        self.verticalLayout_5 = QVBoxLayout(self.dang_nghe)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.NowPlaying = QLabel(self.dang_nghe)
        self.NowPlaying.setObjectName(u"NowPlaying")
        self.NowPlaying.setMinimumSize(QSize(0, 0))
        self.NowPlaying.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(17)
        font4.setBold(False)
        font4.setItalic(True)
        self.NowPlaying.setFont(font4)
        self.NowPlaying.setStyleSheet(u"")
        self.NowPlaying.setFrameShape(QFrame.NoFrame)
        self.NowPlaying.setFrameShadow(QFrame.Plain)
        self.NowPlaying.setLineWidth(1)

        self.verticalLayout_5.addWidget(self.NowPlaying)


        self.horizontalLayout_5.addWidget(self.dang_nghe)

        self.dieu_khien = QWidget(self.bottom)
        self.dieu_khien.setObjectName(u"dieu_khien")
        self.dieu_khien.setMinimumSize(QSize(330, 50))
        self.dieu_khien.setMaximumSize(QSize(16777215, 50))
        self.dieu_khien.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.dieu_khien)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.nghe_lai = QPushButton(self.dieu_khien)
        self.nghe_lai.setObjectName(u"nghe_lai")
        self.nghe_lai.setMinimumSize(QSize(30, 30))
        self.nghe_lai.setMaximumSize(QSize(30, 30))
        self.nghe_lai.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 0, 0,40);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(0, 0, 0,70);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nghe_lai.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.nghe_lai)

        self.prev = QPushButton(self.dieu_khien)
        self.prev.setObjectName(u"prev")
        self.prev.setMinimumSize(QSize(50, 50))
        self.prev.setMaximumSize(QSize(50, 50))
        self.prev.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 0, 0,40);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(0, 0, 0,70);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/prev1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon5)
        self.prev.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.prev)

        self.button_play = QPushButton(self.dieu_khien)
        self.button_play.setObjectName(u"button_play")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_play.sizePolicy().hasHeightForWidth())
        self.button_play.setSizePolicy(sizePolicy)
        self.button_play.setMinimumSize(QSize(50, 50))
        self.button_play.setMaximumSize(QSize(50, 50))
        self.button_play.setSizeIncrement(QSize(0, 0))
        self.button_play.setBaseSize(QSize(0, 0))
        self.button_play.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 0, 0,40);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(0, 0, 0,70);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_play.setIcon(icon6)
        self.button_play.setIconSize(QSize(30, 30))
        self.button_play.setCheckable(True)
        self.button_play.setChecked(False)
        self.button_play.setAutoDefault(False)
        self.button_play.setFlat(False)

        self.horizontalLayout_6.addWidget(self.button_play)

        self.button_next = QPushButton(self.dieu_khien)
        self.button_next.setObjectName(u"button_next")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy1)
        self.button_next.setMinimumSize(QSize(50, 50))
        self.button_next.setMaximumSize(QSize(50, 50))
        self.button_next.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 0, 0,40);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(0, 0, 0,70);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/next1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_next.setIcon(icon7)
        self.button_next.setIconSize(QSize(16, 16))
        self.button_next.setCheckable(False)
        self.button_next.setChecked(False)

        self.horizontalLayout_6.addWidget(self.button_next)

        self.button_mute1 = QPushButton(self.dieu_khien)
        self.button_mute1.setObjectName(u"button_mute1")
        self.button_mute1.setMinimumSize(QSize(30, 30))
        self.button_mute1.setMaximumSize(QSize(30, 30))
        self.button_mute1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 0, 0,40);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(0, 0, 0,70);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/volume-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_mute1.setIcon(icon8)
        self.button_mute1.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.button_mute1)


        self.horizontalLayout_5.addWidget(self.dieu_khien)

        self.am_luong_and_nghe_lai = QWidget(self.bottom)
        self.am_luong_and_nghe_lai.setObjectName(u"am_luong_and_nghe_lai")
        self.am_luong_and_nghe_lai.setMinimumSize(QSize(250, 0))
        self.am_luong_and_nghe_lai.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.am_luong_and_nghe_lai)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 9, 0)
        self.button_mute2 = QPushButton(self.am_luong_and_nghe_lai)
        self.button_mute2.setObjectName(u"button_mute2")
        self.button_mute2.setMaximumSize(QSize(30, 16777215))
        self.button_mute2.setStyleSheet(u"background-color:rgba(255, 255, 255, 0);")
        self.button_mute2.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.button_mute2)

        self.slider_volume = QSlider(self.am_luong_and_nghe_lai)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setMinimumSize(QSize(150, 0))
        self.slider_volume.setMaximumSize(QSize(150, 16777215))
        self.slider_volume.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 7px;\n"
"    background: #C0C0C0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:rgb(202, 132, 81);\n"
"    border: none;\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}")
        self.slider_volume.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.slider_volume)


        self.horizontalLayout_5.addWidget(self.am_luong_and_nghe_lai, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.bottom)


        self.verticalLayout.addWidget(self.bot)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_play.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Searcher.setText("")
        self.Searcher.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.nut_enter.setText("")
        self.buttonMyMusic.setText(QCoreApplication.translate("MainWindow", u"My Music", None))
        self.buttonPlaylist.setText(QCoreApplication.translate("MainWindow", u"PlayList", None))
        self.button_Daily_suggest.setText(QCoreApplication.translate("MainWindow", u"Daily Suggest", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TAB HIEN THOI", None))
        self.button_add_file.setText(QCoreApplication.translate("MainWindow", u"ADD FILE", None))
        self.button_Add_Folder.setText(QCoreApplication.translate("MainWindow", u"ADD FOLDER", None))
        self.button_Delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.timepassed.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.timeRemain.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.NowPlaying.setText(QCoreApplication.translate("MainWindow", u"Now: Dusk Till Dawn", None))
        self.nghe_lai.setText("")
        self.prev.setText("")
        self.button_play.setText("")
        self.button_next.setText("")
        self.button_mute1.setText("")
        self.button_mute2.setText("")
    # retranslateUi


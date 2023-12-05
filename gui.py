"""
:Author: Seth Johnson
:Date: 11-29-2023
:Description:

This script provides the strcuture to generate a GUI that displays the layout of a TV remote
The GUI provides features for the following actions:
    Turning on and off the TV
    Muting and unmuting the TV
    Incramenting and decramenting the TV channel
    Incramenting and decramenting the TV volume
    0-9 keypad to allow disctrete channel selection
"""
### Import packages ###
from PyQt6 import QtCore, QtGui, QtWidgets

### Class definition ###
class RemoteGUI(object):
    """
    GUI class that configures and builds the GUI for the TV remote
    Attributes
    ----------
    centralwidget : QWidget
        widget object that will possess all other widgets for this GUI
    buttonPOWER : QPushButton
        calls the TVRemote.power() method
    buttonMUTE : QPushButton
        calls the TVRemote.mute() method
    buttonCHUP : QPushButton
        calls the TVRemote.channel_up() method
    buttonCHDWN : QPushButton
        calls the TVRemote.channel_down() method
    buttonVOLUP : QPushButton
        calls the TVRemote.volume_up() method
    buttonVOLDWN : QPushButton
        calls the TVRemote.volume_down() method
    button0 : QPushButton
        calls the TVRemote.set_channel(0) method
    button1 : QPushButton
        calls the TVRemote.set_channel(1) method
    button2 : QPushButton
        calls the TVRemote.set_channel(2) method
    button3 : QPushButton
        calls the TVRemote.set_channel(3) method
    button4 : QPushButton
        calls the TVRemote.set_channel(4) method
    button5 : QPushButton
        calls the TVRemote.set_channel(5) method
    button6 : QPushButton
        calls the TVRemote.set_channel(6) method
    button7 : QPushButton
        calls the TVRemote.set_channel(7) method
    button8 : QPushButton
        calls the TVRemote.set_channel(8) method
    button9 : QPushButton
        calls the TVRemote.set_channel(9) method
    volumeBar : QProgressBar
        displays the volume value in percentage by calling TVRemote.getVolume()    
    
    Methods
    -------
    setupGUI(window: QWidget):
        Generates widgets and window default state
    """
    def setupGUI(self, window) -> None:
        ### Window presets ###
        window.setWindowTitle("TV Remote")
        window.setFixedSize(303, 455)
        self.centralwidget = QtWidgets.QWidget(parent=window)

        ### Generating Widgets ###
        # Volume bar
        self.volumeBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.volumeBar.setGeometry(QtCore.QRect(60, 80, 171, 23))
        self.volumeBar.setProperty("value", 0)
        
        # Channel Buttons
        # Button 1
        self.button1 = QtWidgets.QPushButton("1", parent=self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(90, 240, 31, 25))
        # Button 2
        self.button2 = QtWidgets.QPushButton("2", parent=self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(130, 240, 31, 25))
        # Button 3
        self.button3 = QtWidgets.QPushButton("3", parent=self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(170, 240, 31, 25))
        # Button 4
        self.button4 = QtWidgets.QPushButton("4", parent=self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(90, 280, 31, 25))
        # Button 5
        self.button5 = QtWidgets.QPushButton("5", parent=self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(130, 280, 31, 25))
        # Button 6
        self.button6 = QtWidgets.QPushButton("6", parent=self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(170, 280, 31, 25))
        # Button 7
        self.button7 = QtWidgets.QPushButton("7", parent=self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(90, 320, 31, 25))
        # Button 8
        self.button8 = QtWidgets.QPushButton("8", parent=self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(130, 320, 31, 25))
        # Button 9
        self.button9 = QtWidgets.QPushButton("9", parent=self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(170, 320, 31, 25))
        # Button 0
        self.button0 = QtWidgets.QPushButton("0", parent=self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(130, 360, 31, 25))
        
        # Directional buttons
        # Channel UP
        self.buttonCHUP = QtWidgets.QPushButton("CH", parent=self.centralwidget)
        self.buttonCHUP.setGeometry(QtCore.QRect(130, 130, 31, 25))
        # Channel DOWN
        self.buttonCHDWN = QtWidgets.QPushButton("CH", parent=self.centralwidget)
        self.buttonCHDWN.setGeometry(QtCore.QRect(130, 190, 31, 25))
        # Volume UP
        self.buttonVOLUP = QtWidgets.QPushButton("VOL", parent=self.centralwidget)
        self.buttonVOLUP.setGeometry(QtCore.QRect(170, 160, 31, 25))
        # Volume DOWN
        self.buttonVOLDWN = QtWidgets.QPushButton("VOL", parent=self.centralwidget)
        self.buttonVOLDWN.setGeometry(QtCore.QRect(90, 160, 31, 25))

        # State buttons
        # Power button
        self.buttonPOWER = QtWidgets.QPushButton("I/O", parent=self.centralwidget)
        self.buttonPOWER.setGeometry(QtCore.QRect(30, 30, 31, 25))
        # Mute Button
        self.buttonMUTE = QtWidgets.QPushButton("MUTE", parent=self.centralwidget)
        self.buttonMUTE.setGeometry(QtCore.QRect(230, 30, 41, 25))

        ### Assemble our window ###
        window.setCentralWidget(self.centralwidget) # assigning the Window's central widget GUI.centralwidget
        QtCore.QMetaObject.connectSlotsByName(window) # Compiling window metaobject
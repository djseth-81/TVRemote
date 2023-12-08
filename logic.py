"""
:Author: Seth Johnson
:Date: 11-20-2023
:Description:
This script houses the object TVRemote to represent the behavior commonly found on TV remotes. It is called in by the GUI for operation.
"""

### Import packages ###
from PyQt6.QtWidgets import *
from gui import *

### Class definition ###
class TVRemote(QMainWindow, RemoteGUI):
    """
    A class representing the function of a Television remote. It is initiated by main.py
    This class calls upon gui.GUI() when initialized, generating a GUI object by calling setupGUI()

    Attributes
    ----------
    status : bool
        Determines if the television (tv) is powered on or not
    muted : bool
        Determines if the tv has been muted, reverting the volume value to 0
    volume : int
        Represents the volume of the tv
    channel : int
        Represents the selected channel of the tv
    
    Methods
    -------
    power():
        Toggles the status boolean to turn the tv on and off
    mute():
        Toggles the muted boolean to mute and unmute the tv. When the tv is muted, the volume is displayed as 0
    channel_up():
        Incraments the channel variable until the maximum channel value is reached, after which cycles back to the minimum channel value.
    channel_down():
        Decraments the channel variable until the minimum channel value is reached, after which it cycles to the maximum channel value
    volume_up():
        Incraments the volume variable until the maximum volume value is reached.
    volume_down():
        Decrements the volume variable until the minimum volume vaule is reached.
    set_channel(value: int):
        Assigns 
    powered():
        Returns the state of the status boolean
    muted():
        Returns the state of the muted boolean
    getVolume():
        Returns the integer value of volume
    getChannel():
        Returns the integer value of channel
    __str__():
        returns a formatted string which calls getDevice(), powered(), muted(), getChannel(), and getVolume() to display the given state of a tv object
    """

    ### Class Variables ###
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 100 #increased value to represetn 100% volume
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 9 # increased value for all button functionality

    ### Constructors ###
    def __init__(self) -> None:
        """
        Constructs the instance attributes for the tv object
        """
        super().__init__() # we need access to widget functions called from QWidgets, which GUI is a child of

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = TVRemote.MIN_VOLUME
        self.__channel: int = TVRemote.MIN_CHANNEL

        self.setupGUI(self) # configures GUI object by calling PromptWindow.setupGUI()

        ### Buttion actions ###
        self.buttonPOWER.clicked.connect(lambda : self.power())
        self.buttonMUTE.clicked.connect(lambda : self.mute())

        self.buttonCHUP.clicked.connect(lambda : self.channel_up())
        self.buttonVOLUP.clicked.connect(lambda : self.volume_up())
        self.buttonCHDWN.clicked.connect(lambda : self.channel_down())
        self.buttonVOLDWN.clicked.connect(lambda : self.volume_down())

        self.button0.clicked.connect(lambda : self.set_channel(0))
        self.button1.clicked.connect(lambda : self.set_channel(1))
        self.button2.clicked.connect(lambda : self.set_channel(2))
        self.button3.clicked.connect(lambda : self.set_channel(3))
        self.button4.clicked.connect(lambda : self.set_channel(4))
        self.button5.clicked.connect(lambda : self.set_channel(5))
        self.button6.clicked.connect(lambda : self.set_channel(6))
        self.button7.clicked.connect(lambda : self.set_channel(7))
        self.button8.clicked.connect(lambda : self.set_channel(8))
        self.button9.clicked.connect(lambda : self.set_channel(9))

    ### Mutators ###
    def power(self) -> None:
        """
        Toggles the status boolean to turn the tv on and off
        """
        self.__status = False if self.powered() else True
        
    def mute(self) -> None:
        """
        Toggles the mute boolean to mute and unmute the tv.
        """
        if self.powered():
            if self.muted():
                self.__muted = False
                self.volumeBar.setProperty("value", self.getVolume())
            else:
                self.__muted = True
                self.volumeBar.setProperty("value", 0)

    def channel_up(self) -> None:
        """
        Incraments the channel variable until the maximum channel value is reached, after which cycles back to the minimum channel value.
        """
        if self.powered():
            if self.__channel < TVRemote.MAX_CHANNEL:
                self.__channel += 1
            else:
                # If on maximum channel value and called again, cycles back to min channel value
                self.__channel = TVRemote.MIN_CHANNEL
        
    def channel_down(self) -> None:
        """
        Decraments the channel variable until the minimum channel value is reached, after which it cycles to the maximum channel value
        """
        if self.powered():
            if self.__channel > TVRemote.MIN_CHANNEL:
                self.__channel -= 1
            else:
                # Cycles back to max channel called at min value
                self.__channel = TVRemote.MAX_CHANNEL
        
    def volume_up(self) -> None:
        """
        Incraments the volume variable until the maximum volume value is reached.
        """
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume < TVRemote.MAX_VOLUME:
                self.__volume += 1
        self.volumeBar.setProperty("value", self.getVolume())
    
    def volume_down(self) -> None:
        """
        Decrements the volume variable until the minimum volume vaule is reached.
        """
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume > TVRemote.MIN_VOLUME:
                self.__volume -= 1
        self.volumeBar.setProperty("value", self.getVolume())
        
    def set_channel(self, value: int) -> None:
        """
        Activates upon a user pressing one of the number buttons. Each button assigns it's value to the channel variable
        :param value: The integer value representing a user-inputted channel
        """
        if self.powered():
            self.__channel = value

    ### Accessors ###
    def powered(self) -> bool:
        """
        Returns the state of the status boolean
        :return: self.__status
        """
        return self.__status

    def muted(self) -> bool:
        """
        Returns the state of the muted boolean
        :return: self.__muted
        """
        return self.__muted

    def getVolume(self) -> int:
        """
        Returns the integer value of volume
        :return: 0 if the tv is muted or self.__volume otherwise
        """
        return 0 if self.muted() else self.__volume
        
    def getChannel(self) -> int:
        """
        Returns the integer value of channel
        :return: self.__channel
        """
        return self.__channel
        
    def __str__(self) -> str:
        """
        Returns a formatted string which calls powered(), getChannel(), and getVolume() to display the given state of a tv object
        :return: string of the power status, channel value, and volume value
        """
        return f"Power - {self.powered()}, Mute - {self.muted()}, Channel - {self.getChannel()}, Volume - {self.getVolume()}"

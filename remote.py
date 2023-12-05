"""
:Author: Seth Johnson
:Date: 11-13-2023
:Description:
This script houses the methods used in TVRemote in logic.py. This is called in test_television.py to test their behavior
"""

### Class definition ###
class Television:
    

    ### Class Variables ###
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int= 0
    MAX_CHANNEL: int= 3

    ### Constructors ###
    def __init__(self) -> None:
        """
        Constructs the instance attributes for the tv object
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

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
        # Increments tv channel value when tv is on
        if self.powered():
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                # If on maximum channel value and called again, cycles back to min channel value
                self.__channel = self.MIN_CHANNEL
    
    def channel_down(self) -> None:
        """
        Decraments the channel variable until the minimum channel value is reached, after which it cycles to the maximum channel value
        """
        # Decrements tv channel value when tv is on.
        if self.powered():
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                # Cycles back to max channel called at min value
                self.__channel = self.MAX_CHANNEL
    
    def volume_up(self) -> None:
        """
        Incraments the volume variable until the maximum volume value is reached.
        """
        # incraments tv volume when tv is on. remains at maximum when called at max value
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """
        Decrements the volume variable until the minimum volume vaule is reached.
        """
        # decrements tv volume when tv is on. remains at min value when called at min value
        if self.powered():
            if self.muted():
                # automatically unmutes tv
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

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

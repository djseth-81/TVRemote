"""
:Author: Seth Johnson
:Date: 11-20-2023
:Description:
This script executes unit testing with the PyTest module to verify the behavior of the methods within television.py
"""
### Import packages ###
import pytest
from television import Television

### Test class ###
class Test:

    ### Setup and teardown ###
    def setup_method(self):
        """
        Configures the objects tv1 and tv2 for use in each of the test cases.
        """
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        """
        Removes the tv1 and tv2 objects after each test case has been completed to keep each interaciton isolated.
        """
        del self.tv1
        del self.tv2

    ### Test cases ###
    def test_construction(self):
        """
        This tests the construction of the television (tv) class of which the variables, tv1 and tv2, have been assigned.
        """
        # Verifying that the values are initalized properly
        assert self.tv1.__str__() == "Power - False, Channel - 0, Volume - 0"
        assert self.tv2.__str__() == "Power - False, Channel - 0, Volume - 0"

    def test_power(self):
        """
        This tests the power behavior of the tv object. It tests that the object can be toggled from False, to True, and then back to False.
        """
        # Verifying behavior when power is flipped to True
        self.tv1.power() # powered() == True
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"

        # Verifying behavior when power is flipped back to False
        self.tv1.power() # powered() == False
        assert self.tv1.__str__() == "Power - False, Channel - 0, Volume - 0"

    def test_mute(self):
        """
        This tests the mute behavior of the tv object. It checks for the behavior when the tv object has been powered off, and it's behavior with non-zero volume values while the object is powered on.
        """
        # Verifying behavior when tv is on, vlume is increased above 0, then muted
        self.tv1.power() # powered() == True
        self.tv1.volume_up() # getVolume() == 1
        self.tv1.mute() # muted() == True
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"

        # Verifying behavior when tv is on and unmuted
        self.tv1.mute() # muted() == False
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 1"
        
        # Verifying behavior when tv is off and muted
        self.tv2.mute() # muted() == False b/c power is False
        assert self.tv2.__str__() == "Power - False, Channel - 0, Volume - 0"
        
        # Verifying behavior when tv is off and unmuted
        self.tv2.mute() # muted() == False b/c power is still False
        assert self.tv2.__str__() == "Power - False, Channel - 0, Volume - 0"

    def test_channel_up(self):
        """
        This tests how the object handles incramenting the channel value. It tests while the tv object is off, when the tv object is on, and how it handles reaching a maximum value.
        """
        # verifying behavior when tv is off, channel does not incrament
        self.tv1.channel_up() # channel should still equal 0, since power is False
        assert self.tv1.__str__() == "Power - False, Channel - 0, Volume - 0"

        # verifying behavior when tv is on, channel is incramented
        self.tv1.power() # powered() == True
        self.tv1.channel_up() # getChannel() == 1
        assert self.tv1.__str__() == "Power - True, Channel - 1, Volume - 0"
        
        # verifying behavior when tv is on, channel_up cycles back to 1st channel
        self.tv1.channel_up() # getChannel() == 2
        assert self.tv1.__str__() == "Power - True, Channel - 2, Volume - 0"
        self.tv1.channel_up() # getChannel() == 3; now at max channel
        assert self.tv1.__str__() == "Power - True, Channel - 3, Volume - 0"
        self.tv1.channel_up() # getChannel() == 0; back to first channel
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"
        
    def test_channel_down(self):
        """
        Like test_channel_up, this method tests the object's behavior when decrementing its channel value. It accounts for when the tv is powered off, when it is powered on, and what happens when it reaches a minimum value.
        """
        # verifying behavior when tv is off, channel does not incrament
        self.tv1.channel_down() # channel should still equal 0, since power is False
        assert self.tv1.__str__() == "Power - False, Channel - 0, Volume - 0"

        # verifying behavior when tv is on, channel_down cycles to max channel
        self.tv1.power() # powered() == True
        self.tv1.channel_down() # getChannel() == 3; max channel since it was at min channel already
        assert self.tv1.__str__() == "Power - True, Channel - 3, Volume - 0"
        
        # verifying behavior when tv is on, channel_down decrements
        self.tv1.channel_down() # getChannel() == 2
        assert self.tv1.__str__() == "Power - True, Channel - 2, Volume - 0"
        self.tv1.channel_down() # getChannel() == 1
        assert self.tv1.__str__() == "Power - True, Channel - 1, Volume - 0"
        self.tv1.channel_down() # getChannel() == 0; now back to min channel
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"

    def test_volume_up(self):
        """
        Similar to test_channel_up, this tests the tv object's behavior when incramenting its volume value. In addition to handling the power state, as well as it's maximum value, it also accounts for whether the tv has been muted.
        """
        # Verifying behavior when tv is off, volume does not increase
        self.tv1.volume_up() # getVolume() == 0, since powered() == False
        assert self.tv1.__str__() == "Power - False, Channel - 0, Volume - 0"

        # Verifying behavior when tv is on, volume is incramented
        self.tv1.power() # powered() == True
        self.tv1.volume_up() # getVolume() == 1
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 1"
        
        # Verifying behavior when tv is on, muted, volume incraments and unmutes
        self.tv1.mute() # muted() == True, getVolume() == 0
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"
        self.tv1.volume_up() # muted() == False, getVolume() == 2
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 2"
        
        # Verifying behavior when tv is on, volume does not incrament past maximum value
        self.tv1.volume_up() # getVolume() == 2; shouldn't breach maximum value
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 2"

    def test_volume_down(self):
        """
        Similar to test_channel_down, this tests the tv object's behavior while decramenting it's volume value. Like test_volume_up, it accounts for the powered state, the muted state, as well as when the value reaches it's minimum.
        """
        # Verifying behavior when tv is off, volume does not decreacse
        self.tv1.volume_up() # getVolume() == 0, since powered() == False
        assert self.tv1.__str__() == "Power - False, Channel - 0, Volume - 0"

        # Verifying behavior when tv is on, volume is decremented
        self.tv1.power() # powered() == True
        self.tv1.volume_up() # getVolume() == 1
        self.tv1.volume_down() # getVolume() == 0
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"
        
        # Verifying behavior when tv is on, muted, volume decrements and unmutes
        self.tv1.volume_up() # getVolume() == 1
        self.tv1.volume_up() # getVolume() == 2
        self.tv1.mute() # muted() == True, getVolume() == 0
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"
        self.tv1.volume_down() # muted() == False, getVolume() == 1
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 1"
        
        # Verifying behavior when tv is on, volume does not decrement past minimum value
        self.tv1.volume_down() # getVolume() == 0; at minimum value
        self.tv1.volume_down() # getVolume() == 0; shouldn't breach minimum value
        assert self.tv1.__str__() == "Power - True, Channel - 0, Volume - 0"

    def test_channel_select(self):
        # Testing behavior when power is off
        self.tv1.set_channel(6) # getChannel() should still be 0
        assert self.tv1.__str__() == "Power - False, Mute - False, Channel - 0, Volume - 0"
        # Testing behavior when power is on, and channel is 0
        self.tv1.power()
        self.tv1.set_channel(5) # channel should be set at minimum value as clarified from init_test(), this tests assignment while @ min value as well
        assert self.tv1.__str__() == "Power - True, Mute - False, Channel - 5, Volume - 0"
        # Testing behavior when power is on, channel is non-zero
        self.tv1.set_channel(2)
        assert self.tv1.__str__() == "Power - True, Mute - False, Channel - 2, Volume - 0"
        # Testing behavior when power is on, channel is max
        self.tv1.set_channel(9) # setting to max
        assert self.tv1.__str__() == "Power - True, Mute - False, Channel - 9, Volume - 0"
        self.tv1.set_channel(0) # setting to min just to test both behavior @ max and the behavior of setting to min
        assert self.tv1.__str__() == "Power - True, Mute - False, Channel - 0, Volume - 0"
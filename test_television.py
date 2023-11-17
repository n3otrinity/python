import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()
        self.tv3 = Television()
        self.tv4 = Television()
        self.tv5 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2
        del self.tv3
        del self.tv4
        del self.tv5

    def test_init(self):
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.mute()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.mute()
        self.tv1.power()
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.tv2.channel_up()
        assert str(self.tv2) == 'Power = False, Channel = 0, Volume = 0'
        self.tv2.power()
        self.tv2.channel_up()
        assert str(self.tv2) == 'Power = True, Channel = 1, Volume = 0'
        self.tv2.channel_up()
        self.tv2.channel_up()
        self.tv2.channel_up()
        assert str(self.tv2) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv3.channel_down()
        assert str(self.tv3) == 'Power = False, Channel = 0, Volume = 0'
        self.tv3.power()
        self.tv3.channel_down()
        assert str(self.tv3) == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        self.tv4.volume_up()
        assert str(self.tv4) == 'Power = False, Channel = 0, Volume = 0'
        self.tv4.power()
        self.tv4.volume_up()
        assert str(self.tv4) == 'Power = True, Channel = 0, Volume = 1'
        self.tv4.mute()
        self.tv4.volume_up()
        assert str(self.tv4) == 'Power = True, Channel = 0, Volume = 0'
        self.tv4.mute()
        self.tv4.volume_up()
        assert str(self.tv4) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv5.volume_down()
        assert str(self.tv5) == 'Power = False, Channel = 0, Volume = 0'
        self.tv5.power()
        self.tv5.volume_up()
        self.tv5.volume_up()
        self.tv5.mute()
        self.tv5.volume_down()
        assert str(self.tv5) == 'Power = True, Channel = 0, Volume = 0'
        self.tv5.mute()
        assert str(self.tv5) == 'Power = True, Channel = 0, Volume = 1'
        self.tv5.volume_down()
        self.tv5.volume_down()
        self.tv5.mute()
        self.tv5.volume_down()
        assert str(self.tv5) == 'Power = True, Channel = 0, Volume = 0'




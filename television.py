class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        '''Changes the status of the Television object.'''
        self.__status = not(self.__status)

    def mute(self):
        '''Mutes or unmutes the Television object.'''
        self.__muted = not(self.__muted)

    def channel_up(self):
        '''Increases the Telvision object's current channel value by 1.
        Wraps around back to minimum channel when maximum is reached.'''
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
             self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        '''Decreases the Telvision object's current channel value by 1.
            Wraps around back to maximum channel when minimum is reached.'''
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        '''Increases the Telvision object's current volume value by 1.'''
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''Decreases the Telvision object's current volume value by 1.'''
        if self.__status == True:
         if self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self):
        if self.__muted == True:
            return (f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0')
        else:
            return(f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}')



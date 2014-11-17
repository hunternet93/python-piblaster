# Python pi-blaster interface
# By Isaac Smith 2014-11-16

class PiBlasterError(Exception):
    '''A custom exception for PiBlaster errors.'''
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

class PiBlaster:
    '''The PiBlaster object acts similary to a dictionary, pin values can be set simply by setting them on a PiBlaster instance:
        piblaster = PiBlaster()
        piblaster[22] = 0.5'''

    def __init__(self):
        try:
#            self.device = open('/dev/piblaster', 'w')
#            self.device = open('/dev/null', 'w')
            import sys
            self.device = sys.stdout
        except FileNotFoundError:
            raise PiBlasterError('Could not open /dev/piblaster. Please make sure piblaster is installed and operational.')
        except PermissionError:
            raise PiBlasterError('Permission error opening /dev/piblaster, please give the current user write permissions to /dev/piblaster')
            
        self.valid_pins = [4,17,18,21,22,23,24,25]
        self._pins = {x: 0.0 for x in self.valid_pins}
        
    def setpin(self, pin, value):
        '''Sets a pin to a certain value'''
        if not pin in self.valid_pins:
            raise PiBlasterError('Invalid GPIO pin: ' + str(pin))
            
        if value < 0 or value > 1:
            raise PiBlasterError('Pin value must be between 0 and 1, inclusive.')

        if not self._pins[pin] == value:
            self._pins[pin] = value
            self.device.write(str(pin) + '=' + str(value) + '\n')

    def __get__(self):
        return self._pins
        
    def __getitem__(self, index):
        return self._pins.__getitem__(index)
        
    def __setitem__(self, index, value):
        if type(index) == int:
            self.setpin(index, value)
        else:
            raise PiBlasterError('Index value must be integer, not slice or list.')

    def __repr__(self):
        return 'PiBlaster('+str(self._pins)+')'

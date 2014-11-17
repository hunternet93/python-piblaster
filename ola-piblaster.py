import piblaster
from ola.ClientWrapper import ClientWrapper

universe = 0
pinmapping = {
    4: 0,
    17: 1,
    18: 2,
    21: 3,
    22: 4,
    23: 5,
    24: 6,
    25: 7
}
    

blaster = piblaster.PiBlaster()

def writeData(data):
    for pin, channel in pinmapping.items():
        try:
            value = round(data[channel] / 255.0, 3)
            blaster[pin] = value
        except IndexError:
            break
            
wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(universe, client.REGISTER, writeData)
wrapper.Run()

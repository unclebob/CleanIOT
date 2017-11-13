from utils.binhex import hexValues3
from utils.spi7191 import *

hub_addr = None
reading = False

@setHook(HOOK_STARTUP)
def startup():
    mcastRpc(1,2,"imAlive")
    print "imAlive"
    snappySpiInit()
    initMonitorAdcReady()
    snappySpiRead(3, 8)

ADC_READY_PIN = 30
ADC_READY = False
EVERY_MS = 3
def initMonitorAdcReady():
    setPinDir(ADC_READY_PIN, False)
    monitorPin(ADC_READY_PIN, True)
    setRate(EVERY_MS)

@setHook(HOOK_GPIN)
def pinChanged(pinNum, isSet):
    global reading
    if not reading:
        return
    if pinNum == ADC_READY_PIN and isSet == ADC_READY:
        readAndSend()

# -- Collector node API functions

def enableCollector():
    snappyADCEnable()
    addr = rpcSourceAddr()
    sendAck(addr, "enableCollector", "-")

def disableCollector():
    snappyADCDisable()
    addr = rpcSourceAddr()
    global reading
    reading = False
    sendAck(addr, "disableCollector", "-")

def readAndReport():
    global reading
    reading = True
    global hub_addr
    hub_addr = rpcSourceAddr()
    sendAck(hub_addr, "readAndReport", "-")

# -- Helpers ---


def sendAck(addr, command, result):
    rpc(addr, "ack", command, result)
    print "ack:" + three_bytes_as_text(addr) + "(" + command + ", " + result + ")"

def echo(this):
    addr = rpcSourceAddr()
    sendAck(addr, "echo", this)
    print "echoing: " + this

def announceHub():
    command = "announceHub"
    addr = rpcSourceAddr()
    print command + ": " + three_bytes_as_text(addr)
    sendAck(addr, "announceHub", "-")

def three_bytes_as_text(addr):
    return hexValues3(ord(addr[0]), ord(addr[1]), ord(addr[2]))

def readAndSend():
    data = snappySpiRead(3, 8)
    print 'SPI read:', three_bytes_as_text(data)
    sendAck(hub_addr, "readAndPrint", three_bytes_as_text(data))


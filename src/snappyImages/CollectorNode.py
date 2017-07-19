from utils.binhex import hexValues3
from utils.spi7191 import *

readPending = False

@setHook(HOOK_STARTUP)
def startup():
    global readPending
    readPending = False
    mcastRpc(1,2,"imAlive")
    print "imAlive"
    snappySpiInit()

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

def startReading():
    global timer
    timer = 3
    global reading
    reading = True

def stopReading():
    global reading
    reading = False

@setHook(HOOK_10MS)
def doEverySec(tick):
    global reading
    global timer
    if reading:
        if timer == 0:
            data = snappySpiRead(3, 8)
            print 'SPI read:', three_bytes_as_text(data)
            timer = 3
        else:
            timer = timer - 1

def enableCollector():
    snappyADCEnable()
    addr = rpcSourceAddr()
    sendAck(addr, "enableCollector", "-")

def disableCollector():
    snappyADCDisable()
    addr = rpcSourceAddr()
    sendAck(addr, "disableCollector", "-")

def readAndPrint():
    addr = rpcSourceAddr()
    data = snappySpiRead(3, 8)
    print 'SPI read:', three_bytes_as_text(data)
    sendAck(addr, "readAndPrint", three_bytes_as_text(data))

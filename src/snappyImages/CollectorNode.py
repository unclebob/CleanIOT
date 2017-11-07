from utils.binhex import hexValues3
from utils.spi7191 import *

readPending = False

@setHook(HOOK_STARTUP)
def startup():
    global read_initiated
    read_initiated = True
    global readPending
    readPending = False
    mcastRpc(1,2,"imAlive")
    print "imAlive"
    snappySpiInit()
    initMonitorAdcReady()

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

ADC_READY_PIN = 30
ADC_READY = False
EVERY_MS = 3
def initMonitorAdcReady():
    setPinDir(ADC_READY_PIN, False)
    monitorPin(ADC_READY_PIN, True)
    setRate(EVERY_MS)

@setHook(HOOK_GPIN)
def pinChanged(pinNum, isSet):
    global read_initiated
    if not read_initiated:
        return
    if pinNum == ADC_READY_PIN and isSet == ADC_READY:
        readAndPrint2()
        read_initiated = False

def readAndPrint2():
    global hub_addr
    data = snappySpiRead(3, 8)
    print 'SPI read:', three_bytes_as_text(data)
    sendAck(hub_addr, "readAndPrint", three_bytes_as_text(data))

def readAndPrint():
    global hub_addr
    hub_addr = rpcSourceAddr()
    readAndPrint2()

def initiateRead():
    global read_initiated
    read_initiated = True
    global hub_addr
    hub_addr = rpcSourceAddr()
    sendAck(hub_addr, "readInitiated", "-")


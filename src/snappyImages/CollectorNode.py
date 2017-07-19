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
    print "ack:" + addr_as_text(addr) + "(" + command + ", " + result + ")"

def echo(this):
    addr = rpcSourceAddr()
    sendAck(addr, "echo", this)
    print "echoing: " + this

def announceHub():
    command = "announceHub"
    addr = rpcSourceAddr()
    print command + ": " + addr_as_text(addr)
    sendAck(addr, "announceHub", "-")

def addr_as_text(addr):
    return hexValues3(ord(addr[0]), ord(addr[1]), ord(addr[2]))

def readThreeBytes():
    global readPending
    readPending = 10

@setHook(HOOK_10MS)
def doEverySec(tick):
    global readPending
    if readPending != 0:
        readPending = readPending - 1

    if readPending == 1:
        data = snappySpiRead(3, 8)
        print 'SPI read:', addr_as_text(data)


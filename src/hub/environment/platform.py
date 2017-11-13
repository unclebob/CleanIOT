import sys
from environment.log import *
from snapconnect import snap

class HubPlatform:
    def __init__(self):
        log = get_log()
        self.platform = sys.platform
        if self.platform == "linux2":
            log.info("Linux")
            # E20 built-in bridge
            self.serial_conn = snap.SERIAL_TYPE_RS232
            self.serial_port = '/dev/snap1'
        elif self.platform == "darwin":
            log.info("Mac")
            # SS200 USB stick on mac
            self.serial_conn = snap.SERIAL_TYPE_SNAPSTICK200
            self.serial_port = 'SnapStick0'
            # self.serial_conn = snap.SERIAL_TYPE_RS232
            # self.serial_port = '/dev/tty.usbserial-A600HH2Z'
            # self.serial_port = '/dev/tty.SLAB_USBtoUART'
        elif self.platform == "win32":
            log.info("Windows")
            # SS200 USB stick on Windows
            self.serial_conn = snap.SERIAL_TYPE_SNAPSTICK200
            self.serial_port = 0
        else:
            log.info("Platform unknown: " + self.platform + " *************************")
            self.serial_conn = "UNKNOWN"
            self.serial_port = 0

import logging
import datetime
import binascii
import os

class HubLog:
    def __init__(self):
        self.log = logging.getLogger(__file__)
        logdir = 'log'
        if not os.path.exists(logdir):
            os.makedirs(logdir)
        consoleHandler = logging.StreamHandler()
        self.log.addHandler(consoleHandler)
        fileHandler = logging.FileHandler(logdir + '/poll.log')
        self.log.addHandler(fileHandler)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fileHandler.setFormatter(formatter)
        consoleHandler.setFormatter(formatter)
        self.log.setLevel(logging.DEBUG)
        logging.getLogger("snaplib.snaplib.EventCallbacks").addHandler(consoleHandler)
        self.log.info("****************************************")


    def addr_as_str(self, addr):
        if addr == 0:
            return "B-CAST" 
        return binascii.hexlify(addr)

    def info(self, message):
        self.log.info(message)

    def sensor(self, addr, message, *stuff):
        info = ": ".join(
                        [self.addr_as_str(addr), str(message).rjust(8, ' ')])
        for s in stuff:
            info += (": " + s)
        self.log.info(info)

    def hub(self, message, *stuff):
        info = "HUB   : "+ message
        for s in stuff:
            info += (": " + s)
        self.log.info(info)

the_log = HubLog()

def get_log():
    return the_log

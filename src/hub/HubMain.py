from time import sleep
from snapconnect import snap
from environment.log import get_log
from environment.platform import HubPlatform

#--- Globals ---
log = get_log()
platform = HubPlatform()

#------ Messages from nodes --------
def imAliveToHub():
    log.sensor(comm.rpc_source_addr(), "", "I'm Alive")
    comm.rpc(comm.rpc_source_addr(), "announceHub")

def ackToHub(command, result):
    sensor_id = comm.rpc_source_addr()
    log.sensor(sensor_id, "ACK", command, result)

def do_menu():
    options = {
        "A" : announceHub,
        "E" : echo,
        "W" : wait_for_replies,
        "Q" : quit,
        }

    while True:
        prompt1 = "A-announce, E-Echo, W-Wait for replies, Q-Quit:"
        command = raw_input(prompt1)
        try:
            options[command.upper()]()
        except KeyError:
            print "What was that?"

#-------- Menu selectable commands ----------
def wait_for_replies():
    count = 3
    print "Wait a few seconds for replies"
    while count > 0:
        poll_a_second()
        count = count - 1

def announceHub():
    comm.mcastRpc(1, 2, 'announceHub',)
    poll_a_second()

def echo():
    comm.mcastRpc(1, 2, "echo", "ping")
    poll_a_second()

def quit():
    exit(0)

#------- Helpers -----------
def poll_a_second():
    POLL_FREQUENCY = 1000
    SLEEP_TIME = 1.0/POLL_FREQUENCY
    global comm
    for _ in xrange(POLL_FREQUENCY):
        comm.poll()
        sleep(SLEEP_TIME)

# --------------------------------------------

def main():
    global comm

    # Add functions that are exposed to the network via RPC
    rpcFuncs = {
                'imAlive' : imAliveToHub,
                'ack' : ackToHub,
                }

    comm = snap.Snap(funcs=rpcFuncs)
    comm.open_serial(platform.serial_conn, platform.serial_port)
    do_menu()

if __name__ == '__main__':
    main() # Run the example


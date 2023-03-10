''' outputs a backwards bar graph. Think of star as the AP and the dashes are distance.
need to change logic on what to do when the bssid isnt located in scan'''

import binascii
import network
import time

nic = network.WLAN(network.STA_IF)
nic.active(True)

def scan_for(bssid_in):
    bssid_scanned = []
    for net in scan:
        ssid = str(net[0].decode('utf-8'))
        bssid = str(binascii.hexlify(net[1], ":").decode('utf-8'))
        bssid = bssid.upper()
        dbm = net[3]
        bssid_scanned.append(bssid)
        
    if bssid_in in bssid_scanned:
        dbm_recording.append(dbm)
        print(dbm_recording)
    else:
        dbm_recording.append(0)
        pass


def trim_list(list_name, limit):
    if len(list_name) > limit:
        list_name.pop(0)
        return list_name


def get_avg(in_list):
    average = sum(in_list)/len(in_list)
    return average


def simple_barchart(in_list):
    dbm = in_list[-1]
    pos_dbm = abs(dbm)
    bar_length = pos_dbm
    bar = f'  {dbm} dbm |' + ("-"  * bar_length) + "*"
    print(bar)


dbm_recording = [0,]

tgt_bssid = "EA:CB:BC:97:86:CF"

while True:
    scan = nic.scan()
    trim_list(dbm_recording, 3)
    scan_for(tgt_bssid)
    simple_barchart(dbm_recording)
    time.sleep(2)




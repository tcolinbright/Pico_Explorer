import network
import binascii
import time
nic = network.WLAN(network.STA_IF)
nic.active(True)
 
n = 4 #number of networks to show (based on strongest singnals in this case)
scan_time = 2 #number of seconds between scans


   
def total_networks_found(scan):
    networks_found = len(scan)
    print(f'Total Networks Found: {networks_found}\n')
    return networks_found

def create_bssid_list(scan):
    bssid_list_full = []
    networks = scan
    for net in networks:
    
        bssid = str(binascii.hexlify(net[1], ":")) #changes hex to normal numbers
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")
        bssid_list_full.append(bssid)
    
    total_aps = len(bssid_list_full)
    print(f'Discovered {total_aps} Access Points\n')
    return bssid_list_full


def get_unique_bssid(input_list):
    for bssid in input_list:
        if bssid in unique_bssid:
            continue
        else:
            unique_bssid.append(bssid)
            bssid_txt = open(r'unique_bssid.txt', 'at')
            bssid_txt.write(f'{bssid}\n')
            bssid_txt.close()
    

def create_ssid_list(scan):
    ssid_list_full = []
    networks = scan
    for net in networks:
        ssid = str(net[0])
        if ssid == "b''":
            ssid = "Hidden"
        else:
            ssid = ssid.replace("b'", "")
            ssid = ssid.replace("'","")
        ssid_list_full.append(ssid)
    
    return ssid_list_full


def get_unique_ssid(input_list):
    for ssid in input_list:
        if ssid in unique_ssid:
            continue
        else:
            unique_ssid.append(ssid)
            ssid_txt = open(r'unique_ssid.txt', 'at')
            ssid_txt.write(f'{ssid}\n')
            ssid_txt.close()


def top_networks(show_top, scan):
    '''Sorts networks by dbm reading and returns the top n amount of them'''
    
    def sort_by_dbm(e):
        return e[3]
    
    networks = scan
    networks.sort(key=sort_by_dbm, reverse=True)
    networks = networks[0:show_top]
    return networks

def formatting(scan_output):
    for net in scan_output:
        
        ssid = str(net[0])
        channel = net[2]
        dbm = net[3]
        #security = str(net[4])
        
        if ssid == "b''":
            ssid = "Hidden"
        else:
            ssid = ssid.replace("b'", "")
            ssid = ssid.replace("'","")
        
        bssid = str(binascii.hexlify(net[1], ":")) #changes hex to normal numbers
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")
       
        print(f'SSID: {ssid}\nBSSID: {bssid} | CH: {channel}  | Dbm: {dbm}\n\n-------------------\n')


def end_scan_line(scan_int):
    print("\n*********\n")
    time.sleep(scan_int)

# Start Here #

unique_bssid = [] # Create empty list of bssid's
unique_ssid = [] # Create empty list of SSID's

while True:
    scan = nic.scan()
    total_networks_found(scan)
    bssid_list = create_bssid_list(scan)
    get_unique_bssid(bssid_list)
    ssid_list = create_ssid_list(scan)
    get_unique_ssid(ssid_list)
    networks = top_networks(n, scan)
    formatting(networks)
    end_scan_line(2)


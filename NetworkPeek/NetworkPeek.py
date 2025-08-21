
import nmap3
import socket

import sys#for args, but also has classes and functions for IP addresses?

#takes a string or float decimal, deletes all the numbers at the end, then appends *
def IPRange(address):
    if(isinstance(address,float)): address = str(address)
    blank = address.rstrip("1234567890")#how tf did I forget 8?  Oh, the 8 on my keyboard is acting up
    final = blank + "*"
    return final

#iterate through the list, check if the port is open and add the number to my own list if it is, and then finally print the list of open ports, raw is a dict, the output of the nmap function
def PrintPorts(raw, IP):
    openPorts = []
    ports = raw.get(IP).get('ports')#ports is a list, a list of dicts I think, god help me

    for port in ports:
        if port['state'] == 'open':
            openPorts.append(port['portid'])
    print("The following ports are open")
    for port in openPorts:
        print(port)#I can't believe I commented this out and forgot about it...

#grab a list of key, which is a list of addresses, then iterate through the output to check if there's a hostname in that entry in the dict, and add the IP address to a list, which it prints at the end, raw is a dict, the output of the nmap function
def PrintDevices(raw):
    activeHosts = []

    count = 0##this is probably not the best way to do this, I'm trying to cycle through key-value pairs and store the keys with the right values.
    for host in raw:#host is the key
        if(count<256 and raw.get(host)['hostname']!=[]):#output ends with three non-address entries, things like runtime, and they throw an error if I try to check them like this
           activeHosts.append(host)
        count+=1
    #aaaaand I forgot to print it LMAO
    print("The scan has found the following addresses:")
    for address in activeHosts:
        print(address)


nmap = nmap3.NmapHostDiscovery()#  What's the difference?  Should I move this down into one of those if statements? 




hostName = socket.gethostname()
IPAddr = socket.gethostbyname(hostName)


scan = False
if(len(sys.argv) == 1):
    print("You can add an IP Adress as an argument, or case-sensitive 'scan' to find all the address on your network.  Defaulting to own address.")
elif sys.argv[1] == "scan":
    scan = True
else:
    IPAddr = sys.argv[1]

if scan:
    IPAddr = IPRange(IPAddr)
    output = nmap.nmap_no_portscan(IPAddr)#faster 
else:
    output = nmap.nmap_portscan_only(IPAddr)
#output = nmap.scan_top_ports(hostName)#it says NMAP isn't installed, but it is! couldn't locate the path?? No, I just needed to close visual studio and reopen it after installing it



#macAddr = output.get(IPAddr).get('macaddress')#says none, and that's not a mistake on my end, it's what's in the dict






if(scan):
    PrintDevices(output)
else:
    PrintPorts(output, IPAddr)

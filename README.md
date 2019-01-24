# APIC-EM
Import devices from .csv into APIC-EM inventory 

# Description
This code is used to upload devices into the APIC-EM inventory utlizing an existing text file.  
The file can simply be a list of IP addresses in the format of devices.txt in this repository.

# Usage
The following parameters must be edited in the script in order to use it.  

#IP address of APIC-EM Contoller
controller='x.w.y.z'

#the username and password to access the APIC-EM Controller
payload = {"username":"apic_username","password":"apic_password"}

The following parameters have default values that can be changed in the payload section of the script to match your environment
payload = {
  "snmpAuthPassphrase": "Cisco123",
  "snmpAuthProtocol": "sha",
  "snmpPrivPassphrase": "Cisco123",
  "snmpPrivProtocol": "aes",
  "snmpROCommunity": "cisco",
  "snmpRWCommunity": "cisco",
  "cliTransport": "ssh",
  "snmpRetry": 3,
  "extendedDiscoveryInfo": "",
  "snmpMode": "authPriv",
  "serialNumber": "",
  "snmpVersion": "v2",
  "userName": "apic",
  "ipAddress": ["192.168.254.254"],
  "password": "Cisco123",
  "enablePassword": "cisco",
  "snmpTimeout": 5,
  "snmpUserName": "kewiggin"
}

The script and the devices.txt file should be placed in the same directory.  

# Files
deviceadd_contest.py - the python script to import devices into the APIC-EM inventory
devices.txt - text file of management IP addresses of devices to be added into APIC-EM

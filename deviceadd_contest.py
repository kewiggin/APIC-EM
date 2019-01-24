#!/usr/bin/env python3

# csv module
import csv

# import requests library
import requests

#import json library
import json

#IP address of APIC-EM Contoller
controller='x.w.y.z'

# put the ip address or dns of your apic-em controller in this url
url = "https://" + controller + "/api/v1/ticket"

#the username and password to access the APIC-EM Controller
payload = {"username":"apic_username","password":"apic_password"}

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket - used for self signed certificates
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
#Use this line if a certificate has been installed on the controller
#response= requests.post(url,data=json.dumps(payload), headers=header)

#convert response to json format
r_json=response.json()

#parse the json to get the service ticket
ticket = r_json["response"]["serviceTicket"]

# URL for Host REST API call
url = "https://" + controller + "/api/v1/network-device"

#Content type must be included in the header as well as the ticket
header = {"content-type": "application/json", "X-Auth-Token":ticket}

#List for updating inventory
newdevices = ['192.168.254.254']

#List for Failed devices
Failures = []

#file for list of failed devices
f= open("failures.txt" ,"w+")

#snmpAuthPassphrase (string): SNMPV3 auth passphrase,
#snmpAuthProtocol (string): SNMPV3 auth protocol. Supported values: sha, md5,
#snmpPrivPassphrase (string): SNMPV3 priv passphrase,
#snmpPrivProtocol (string): SNMPV3 priv protocol. Supported values: des, aes,
#snmpROCommunity (string): SNMP RO community,
#snmpRWCommunity (string): SNMP RW community,
#cliTransport (string): CLI transport. Supported values: telnet, ssh2,
#snmpRetry (integer): SNMP retry count. Max value supported is 3,
#extendedDiscoveryInfo (string, optional),
#snmpMode (string): SNMPV3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv,
#serialNumber (string, optional),
#snmpVersion (string, optional): SNMP version. Values supported: v2, v3. Default is v2,
#userName (string): CLI user name,
#ipAddress (array[string]): IP Address of the device,
#password (string): CLI password,
#enablePassword (string): CLI enable password,
#snmpTimeout (integer): SNMP timeout in seconds (must be greater than 0),
#snmpUserName (string): SNMPV3 user name


#Establish default values for new devices

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


wfh = open('devices.txt','r')
reader = csv.reader(wfh)

for record in reader: #loop through each row

    #assign IP Address to a list
    newdevices[0] = ('{}'.format(record[0]))

    #assign newdevices list to payload dictionary
    payload['ipAddress'] = newdevices

    #print(payload['ipAddress'])

    #Post new device to APIC-EM
    response = requests.post(url,data=json.dumps(payload), headers=header, verify=False)

    #print(response.status_code)
    #Check for failed additions and add to a file
    if response.status_code != 202:
        Failures.append(newdevices[0])
        #print(Failures)

wfh.close()

yy = len(Failures)
print('\n\n\n',yy ,' devices failed to process\n')

# Write failed devices to a file
for i in Failures:
    f.write(str(i)+'\n')
    print(i)
    #print(str(i))
f.close()


exit()

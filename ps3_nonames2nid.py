import sys, os
import struct
from hashlib import sha1
import hashlib
from base64 import b64encode as base64enc
from binascii import unhexlify as uhx

#ref https://github.com/SocraticBliss/ps4_name2nid_plugin

NEW_NIDS = {}
AEROLIB  = 'nids.txt'
NAMES   = 'names.txt'

def noname2nid(name):
    symbol = sha1(name.encode() + "0xbc5eba9e042504905b64274994d9c41f").digest() #O_o
    nid = struct.unpack('<I', symbol[:4])[0]
    NEW_NIDS[nid]=name

def save_nids(NIDS):
    csvFile=open(AEROLIB,"w")
    for nid, name in sorted(NIDS.items(), key=lambda x: x[1]):
        csvFile.writelines('0x%08X %s\n' % (nid, name))
    csvFile.close()



f = open(NAMES,"r")
for line in f.readlines():
    line = line.strip()
    noname2nid(line)

f.close()

save_nids(NEW_NIDS)

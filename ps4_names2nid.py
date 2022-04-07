import sys, os
import struct
#from hashlib import sha1
import hashlib
from base64 import b64encode as base64enc
from binascii import unhexlify as uhx

#ref https://github.com/SocraticBliss/ps4_name2nid_plugin

NEW_NIDS = {}
AEROLIB  = 'aerolib.csv'
NAMES   = 'ps4_names.txt'

def name2nid(name):
    symbol = hashlib.sha1(name.encode() + uhx('518D64A635DED8C1E6B039B1C3E55230')).digest()
    id     = struct.unpack('<Q', symbol[:8])[0]
    nid    = base64enc(uhx('%016x' % id), b'+-').rstrip(b'=')
    NEW_NIDS[nid]=name

def save_nids(NIDS):
    csvFile=open(AEROLIB,"w")
    for nid, name in sorted(NIDS.items(), key=lambda x: x[1]):
        csvFile.writelines('%s %s\n' % (str(nid,'utf-8'), name))
    csvFile.close()



f = open(NAMES,"r")
for line in f.readlines():
    line = line.strip()
    name2nid(line)

f.close()

save_nids(NEW_NIDS)

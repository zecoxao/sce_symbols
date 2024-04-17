import sys, os
import struct
#from hashlib import sha1
import hashlib
from base64 import b64encode as base64enc
from binascii import unhexlify as uhx

#ref https://github.com/SocraticBliss/ps4_name2nid_plugin

NEW_NIDS = {}
AEROLIB  = 'aerolib.csv'
NAMES   = 'ps5_names.txt'
OLD_NIDS = set()


def name2nid(name):
    if name in OLD_NIDS:
        return

    symbol = hashlib.sha1(name.encode() + uhx('518D64A635DED8C1E6B039B1C3E55230')).digest()
    id     = struct.unpack('<Q', symbol[:8])[0]
    nid    = base64enc(uhx('%016x' % id), b'+-').rstrip(b'=')
    NEW_NIDS[nid]=name


def save_nids(nids):
    with open(AEROLIB,"a") as csvFile:
        for nid, name in sorted(nids.items(), key=lambda x: x[1]):
            csvFile.writelines('%s %s\n' % (str(nid,'utf-8'), name))


def fill_old_nids():
    global OLD_NIDS

    def iterate_old_symbols():
        with open(AEROLIB, "r") as f:
            while True:
                line =f.readline()
                if not line:
                    break
                yield line.split()[1]
    OLD_NIDS = {s for s in iterate_old_symbols()}


if __name__ == '__main__':
    fill_old_nids()
    with open(NAMES,"r") as f:
        for line in f.readlines():
            line = line.strip()
            name2nid(line)
    save_nids(NEW_NIDS)

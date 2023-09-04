#!/usr/bin/env python3
# simple script to regex for sce* API names
# in some cases, it is much better to scan all data in the file instead of relying on e.g. nm
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])

names = set()
for path in root.glob('**/*.elf'):
    #print(path)

    data = path.read_bytes()
    match = re.findall(b'sce[A-Z][a-zA-Z0-9]+', data)
    for name in match:
        names.add(str(name, 'ascii'))
    
    # not ideal, but whatever
    data = path.read_text('utf-16le', 'ignore')
    match = re.findall(u'sce[A-Z][a-zA-Z0-9]+', data)
    for name in match:
        names.add(name)
    
    #print(len(names))

for name in sorted(names):
    print(name)

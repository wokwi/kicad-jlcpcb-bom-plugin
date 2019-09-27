#!/usr/bin/env python3
# coding=utf8

# Converts a KiCad Footprint Position (.pos) File into JLCPCB compatible CPL file
# Copyright (C) 2019, Uri Shaked. Released under the MIT license.

import sys
import csv
from collections import OrderedDict

with open(sys.argv[1], 'r') as in_file, open(sys.argv[2], 'w', newline='') as out_file:

    reader = csv.DictReader(in_file)
    ordered_fieldnames = OrderedDict([('Designator',None),('Mid X',None),('Mid Y',None),('Layer',None),('Rotation',None)])
    writer = csv.DictWriter(out_file, fieldnames=ordered_fieldnames)
    writer.writeheader()

    for row in reader:
        writer.writerow({
            'Designator': row['Ref'], 
            'Mid X': row['PosX'] + 'mm', 
            'Mid Y': row['PosY'] + 'mm', 
            'Layer': row['Side'].capitalize(), 
            'Rotation': int(float(row['Rot']))
        })

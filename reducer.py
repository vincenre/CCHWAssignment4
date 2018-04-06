#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


current_veh_type = None
current_count = 0
veh_type = None

for line in sys.stdin:

    line = line.strip()

    veh_type, count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:

        continue
    if current_veh_type == veh_type:
        current_count += count
    else:
        if current_veh_type:
            print ( '%s\t%s' % (current_veh_type, current_count))
        current_count = count
        current_veh_type = veh_type

if current_veh_type == veh_type:
    print( '%s\t%s' % (current_veh_type, current_count))
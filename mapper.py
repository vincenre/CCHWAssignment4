#!/usr/bin/env python
"""mapper.py"""

import sys
count = 0

for line in sys.stdin:
    if(count == 0):
        count = 1
        continue
    
    lineList = line.split(",") 
    type_veh_count = {}
    endIndex = len(lineList)
    startIndex = endIndex - 5
    for j in range(startIndex,endIndex):
        veh_type = lineList[j].strip()
        veh_type = veh_type.strip('\n')
        veh_type = veh_type.strip('\t')
        if (veh_type == "" or '.' in veh_type):
            continue
        print ("%s\t%s" % (veh_type,1))
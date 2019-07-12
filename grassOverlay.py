#!/usr/bin/env python

import grass.script as gscript
import os
from os import path

def main():
    hullDir = "E:\\projects\\londonSidewalksProject\\hullDir\\"
    hullPolygonDir = "E:\\projects\\londonSidewalksProject\\hullPolygonDir\\"
    #count=0

    for hullFile in os.listdir(hullDir):
        if hullFile.endswith(".shp"):
            #count = count + 1
            gscript.run_command('v.in.ogr', input=hullDir+hullFile, output=hullFile[0:-4], flags='o')
            gscript.run_command('v.overlay', ainput='differencePolygon@londonMapset', binput=hullFile[0:-4] + '@londonMapset', operator='and', output=hullFile[0:-4] + 'Overlaid', flags='t')
            gscript.run_command('v.out.ogr', input=hullFile[0:-4] + 'Overlaid@londonMapset', type='area', output=hullPolygonDir+hullFile, format='ESRI_Shapefile')
        #if (count>10):
            #break
if __name__ == '__main__':
    main()

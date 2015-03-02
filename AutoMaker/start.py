import sys
import automarker
import os

testFile='6.png'

if len(sys.argv)==2:
	automarker.generateResult(sys.argv[1])
else:	
	automarker.generateResult(testFile)

os.system('PointsMarker.exe "%s"' % testFile)
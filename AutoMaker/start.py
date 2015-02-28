import sys
import automarker
if len(sys.argv)==2:
	automarker.generateResult(sys.argv[1])
else:	
	automarker.generateResult('badline.png')
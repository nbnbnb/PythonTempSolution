import sys
import automarkerdebug
import os

if len(sys.argv) == 2:
	automarkerdebug.generateResult(sys.argv[1])
else:
    print('Start Marking...')
    #testFiles = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','a.png','b.png']
    testFiles = ['1.png']
    for testFile in testFiles:
        automarkerdebug.generateResult(testFile)
        os.system('PointsMarker.exe "%s"' % testFile)
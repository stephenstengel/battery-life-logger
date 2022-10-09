#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logger.py
#  
#  Copyright 2022 Stephen Stengel <stephen.stengel@cwu.edu>

import datetime
import time


def main(args):
	outFileName = "time-to-death.txt"
	timeToSleep = 1   # in seconds
	
	print("Hi!")
	print("This program will run until canceled with ctrl-c or the" \
			+ " battery dies.")
	print("The total runtime of the battery will be recorded in a " \
			+ "file named: \n" + outFileName)
	
	runLogger(outFileName, timeToSleep)

	return 0


def runLogger(outFileName, timeToSleep):
	startingSeconds = time.time()
	
	while(True):
		with open(outFileName, "w") as timeLog:
			outputLine = "Last clock time: "
			outputLine += str(time.asctime(time.localtime())) + "\n"
			outputLine += "Elapsed time in seconds: "
			outputLine += str(int(time.time() - startingSeconds)) + "\n"
			
			timeLog.write(outputLine)
			timeLog.flush() ## This is needed to write to the file before closing the file.

			time.sleep(timeToSleep)


if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

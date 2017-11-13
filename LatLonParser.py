# LatLonParser
# Written by Scott Kildall
# looks for 




# initialize the pygame environment, which we use to display an image
def process(inputFilename, outputFilename):
	hasHeader = False
	
	inputLines = loadLines(inputFilename)

	outputLines = []


	# output filename
	wf = makeWriteFile( outputFilename )


	# convert each line
	for i in range(0, len(inputLines)):
		

		# check first line for a header, if we have one flag it for output and then skip
		if i == 0:
			if "," not in inputLines[i]:
				print "Has Header: " + inputLines[i] 
				hasHeader = True
				outputLines.append("Latitude, Longitude\n")
				continue
			else:
				print "No Header"

		# append to output lines list
 		outputLines.append (inputLines[i]) 
 		

 	writeLines(wf,outputLines)

    # show output
	numLines = len(inputLines)

	if hasHeader == True:

		print "Success!"
		print "Wrote header"
		print "Wrote " + str(numLines - 1) + " lines"

	else:
		print "Success!"
		print "Wrote " + str(numLines) + " lines"
    	


# load all lines into an array
def loadLines(filename):
	f = open( filename, "r" )
	lines = []
	for line in f:
		# do additional line-processing here
		#lines.append( line.rstrip('\n') )
		lines.append(line)

	f.close()
	return lines



def writeLines(f, lines):
	for line in lines:
		f.write(line)
	f.flush()


def makeWriteFile(filename):
	f = open( filename, "w" )
	return f


# execution point
# input file = input.csv
# output file = output.csv
process("input.csv", "output.csv")



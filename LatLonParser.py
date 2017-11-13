# LatLonParser
# Written by Scott Kildall
# looks for 




# initialize the pygame environment, which we use to display an image
def process(inputFilename, outputFilename):
	hasHeader = False

	# each line in array is 1 line in file	
	inputLines = loadLines(inputFilename)

	# array of output lines
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
				outputLines.append("Latitude, Longitude")
				continue
			else:
				print "No Header"

		# append to output lines list
		inputStr = inputLines[i]

		# check for leading quote
		if inputStr[0] == '"':
			secondCharIndex = inputStr[1:].index('"')

			if secondCharIndex == -1:
				print "Error parsing string at line: " + str(i)
				return


			print secondCharIndex
			
			
			inputStr = inputStr[1:secondCharIndex]
			
			print inputStr

 		outputLines.append(inputStr) 
 		

 	writeLines(wf,outputLines)

    # show output - number of lines, etc
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
		f.write(line + "\n")
	f.flush()


def makeWriteFile(filename):
	f = open( filename, "w" )
	return f


# execution point
# input file = input.csv
# output file = output.csv
process("input.csv", "output.csv")



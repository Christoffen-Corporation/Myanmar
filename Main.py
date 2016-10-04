from Definitions.Main import * # Import everything from all subfiles containing defined vars

with open(InputFile) as f: # Open input file from a JSON string as a value 
      lines = len(f.readlines()) # "lines" outputs the #s of lines in a file
	  
f = open(InputFile) # Assign 'f'

# Solidify 'lines' by assigning it to an int called lines_left
lines_left = lines

"""
We use 'check' to create a check/balance system. We make 'check' an empty 
variable (at zero) that will get modified. This variable SHOULD also give a line 
count accurately. We use it in conjunction with 'lines_left' to tell the loop to
keep iterating as long as check isn't equal to 'lines_left.'
"""
check = 0 

"""
This may as well be most of the program until I can figure out how to break this 
up into its own set of functions or whatnot. The loop starts here and ends the file.
"""
while check < lines_left: # This was explained above 'check'
	file = open(OutputFile, 'w') # The file to output translated language to
	"""
	The current way to use the input is to create a dict and assign it the name 
	"text." This will allow us to search for keys in one file and output them as
	mods in the 'InputFile.'
	"""

	if CheckHeaders == "true":
		with open(OpenHeaders) as header:  
      			header = header.readline() 
		print >> file, str(header) + "\n"

	with open(InputFile) as f: # The file to be converted to another language
		for text in list(f): 
			# Convert else if from one lang to the next
			if FromElseIf in text:
				# Replace From to To (see JSON)
				ElseIf1 = text.replace(FromElseIf, ToElseIf) 
				# Marks where each start lang starts the statement
				ElseIf2 = ElseIf1.replace(FromElseIfStart, ToElseIfStart) 
				# Output modded format to 'InputFile'
				print >> file, ElseIf2
			# 'TextStart' denotes the print()/printf() funcs found in most langs
			if FromTextStart in text: 
				#TODO: Separate this to detect in settings instead
				"""
				These are boilerplates that SHOULD NOT have been put here.
				They should instead be checked for. We should split the file into
				sections instead.
				"""
				print >> file, EntryPointStart 

				Text1 = text.replace(FromTextStart, ToTextStart)
				Text2 = Text1.replace(FromTextStop, ToTextStop)

				print >> file, Text2 
				print >> file, EntryPointStop
			
	file.close()
	check = check + 1
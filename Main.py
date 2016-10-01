from Definitions.Main import *

with open(InputFile) as f:
      lines = len(f.readlines())
	  
f = open(InputFile)
		
lines_left = lines
check = 0

while check < lines_left:	
	file = open(OutputFile, 'w')
	with open(InputFile) as f:
		for text in list(f):
			if FromElseIf in text:
				ElseIf1 = text.replace(FromElseIf, ToElseIf)
				ElseIf2 = ElseIf1.replace(FromElseIfStart, ToElseIfStart)
				print >> file, ElseIf2
			if FromTextStart in text:
				print >> file, Includes + "\n"
				print >> file, EntryPointStart 

				Text1 = text.replace(FromTextStart, ToTextStart)
				Text2 = Text1.replace(FromTextStop, ToTextStop)

				print >> file, Text2 
				print >> file, EntryPointStop
			
	file.close()
	check = check + 1
	

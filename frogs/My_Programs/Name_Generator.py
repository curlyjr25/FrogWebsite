#!/usr/bin/env python

# This is a program that will generate a random name for the frog website form

from random import randint

fp = open("Names_Test.txt", "r") #randomly generates a line number and saves name into Used_Names.txt
fs = open("Used_Names.txt", "a") 
lines = fp.readlines()
x = len(lines)
y = randint(0, x-1)
i = 0
Name = lines[y]				#probably redundant to have because the for loop does the same thing.  Wasn't sure how to save the out put of the for loop to use in the next for loop.

for line in lines:				
	if i == y:
		print(line)
		fs.write(line)
	i += 1

fp.close()
fs.close()
						
fp = open("Names_Test.txt", "w") #Writes all names not found in Used_Names.txt into Names_Test.txt but it is not working.  Just end up with a blank document.
fp.close()

fp = open("Names_Test.txt", "a")
for lineA in lines:
	if lineA != Name:
		fp.write(lineA)
			
fp.close()						#I get this error  File "<stdin>", line 5
    							#fp.close()	
    							# ^
								#SyntaxError: invalid syntax
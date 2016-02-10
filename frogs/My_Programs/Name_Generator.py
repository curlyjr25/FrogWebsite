#!/usr/bin/env python

# This is a program that will generate a random name for the frog website form

from random import randint

fp = open("Names_Test.txt", "r") 
fs = open("Used_Names.txt", "a") 
lines = fp.readlines()
x = len(lines)
y = randint(0, x-1)
i = 0
Name = lines[y]
for line in lines:				
	if i == y:
		print(line)
		fs.write(line)
	i += 1

fp.close()
fs.close()
						
fp = open("Names_Test.txt", "w") #this part deletes the generated name from the name database

for lineA in lines:
	if lineA != Name:
		fp.write(LineA)
			
fp.close()
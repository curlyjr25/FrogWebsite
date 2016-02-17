#!/usr/bin/env python

# This is a program that will generate a random name for the frog website form


from random import randint

fp = open("Names_Test.txt", "r") 

lines = fp.readlines()
x = len(lines)
y = randint(0, x-1)

fp.close()


fp = open("Names_Test.txt", "w") 
fs = open("Used_Names.txt", "a")

Name = lines.pop(y)
print(Name)
fs.write(Name)				

for i in lines:			
	fp.write(i)
		
fp.close()
fs.close()
					
# coding=utf-8
#import os

a = 0
file = open('usernames.txt')

for line in file:
	l = line.split(',');
	a=0
	for x in l:
		a += 1
		print(str(a) + ": " + x)

file.close()



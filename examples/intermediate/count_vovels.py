#!/usr/bin/python

#  Program to Count the Number of Each Vowel
import sys
a=e=i=o=u=0

if len(sys.argv) != 1: #find the length of arguments passed from command line. 
  string=sys.argv[1] 
else:
  string="elephant" # No arguments passed, choose this as default string

for eachchar in string:
  if eachchar=='a':
      a+=1
  elif eachchar=='e':
      e+=1
  elif eachchar=='i':
      i+=1
  elif eachchar=='o':
      o+=1
  elif eachchar=='u':
      u+=1

print('a:',a)
print('e:',e)
print('i:',i)
print('o:',o)
print('u:',u)


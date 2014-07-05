# -*- coding: utf-8 -*-
#Asking Questions

#getting into the data of the programs
#need 2 learn to do 3 things that may not make sense
#Most of what software does is:
    #1. take in some kind of input from a person
    #2. change it
    #3. print out something to show how it changed

#sofar only been printing
#haven't been able to get any input from a person or change it

print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print "how much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
    #NOTE: Notice that we put a , (comma) at the end of each print line. 
    #This is so that print doesn’t end the line with a new line character 
    #and go to the next line.

#https://docs.python.org/2/library/functions.html#raw_input 
    
#Common Student Questions

#How do I get a number from someone so I can do math?
#That’s a little advanced, but try x = int(raw_input()), which gets the number 
#as a string from raw_input() then converts it to an integer using int().

#I put my height into raw input like raw_input("6'2") but it doesn’t work.
#You don’t put your height in there; you type it directly into your Terminal. 
#First thing is, go back and make the code exactly like mine. Next, run the script, 
#and when it pauses, type your height in at your keyboard. That’s all there is to it.

#Why do you have a new line on line 8 instead of putting it on one line?
#That’s so that the line is less than 80 characters long, which is a style that 
#Python programmers like. You could put it on one line if you like.

#What’s the difference between input() and raw_input()?
#The input() function will try to convert things you enter as if they were 
#Python code, but it has security problems so you should avoid it.

#When my strings print out there’s a u in front of them, as in u'35'.
#That’s how Python tells you that the string is Unicode. Use a %s format 
#instead and you’ll see it printed like normal.
# -*- coding: utf-8 -*-
x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." %x 
print "I also said: '%s'" %7

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation %hilarious

w = "This is the left side of ...."
e = "a string with a right side."

print w + e

#What is the difference between %r and %s?
#We use %r for debugging, since it displays the “raw” data of the variable, 
#but we use %s and others for displaying to users.

#What’s the point of %s and %d when you can just use %r?
#The %r is best for debugging, and the other formats are for 
#actually displaying variables to users.

#If you thought the joke was funny could you write hilarious = True? 
#Yes, and you’ll learn more about these boolean values in Exercise 27.

#Why do you put ' (single-quotes) around some strings and not others?
#Mostly it’s because of style, but I’ll use a single-quote inside a string that 
#has double-quotes. Look at line 10 to see how I’m doing that.

#I get the error TypeError: not all arguments converted during string formatting. 
#You need to make sure that the line of code is exactly the same. What happens in 
#this error is you have more % format characters in the string than variables to put 
#in them. Go back and figure out what you did wrong.
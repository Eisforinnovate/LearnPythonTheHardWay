# -*- coding: utf-8 -*-
#Exercise 12-Prompting People

#when you type "raw_input()", you were type the (and) characters, which are parenthesis characters
#similar 2 when you used them to do that formate with extra vars as in:
     
        # "%s %s" % (x,y).

#for raw_input, can also put in a prompt 2 show a person so they know what they typed
#put a string that you want for the prompt side the () so that it looks like:
     
        # y= raw_input("Name?")
        
#This prompts the users with "Name?" and puts result into var y.
#This is how you ask someone a question && get an answer
#This means we can completely rewrite previous exercises using just raw_input
#to do all the prompting

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So you're %r old, %r tall & %r heavy." % (age, height, weight)

#Common Student Questions

#How come I get SyntaxError: invalid syntax whenever I run pydoc?
#You aren’t running pydoc from the command line; you’re probably 
#running it from inside python. Exit out of python first.

#Why does my pydoc not pause like yours does?
#Sometimes if the help document is short enough to fit on one screen, then pydoc will just print it.

#When I run pydoc I get more is not recognized as an internal.
#Some versions of Windows do not have that command, which means pydoc is broken 
#for you. You can skip this Study Drill and just search online for Python documentation when you need it.

#Why would I use %r over %s?
#Remember, %r is for debugging and is “raw representation” while %s is for display. 
#I will not answer this question again, so you must memorize this fact. T
#his is the #1 thing people ask repeat- edly, and asking the same question
#over and over means you aren’t taking the time to memorize what you should
#Stop now, and finally memorize this fact.

#Why can’t I do print "How old are you?" , raw_input()?
#You’d think that’d work, but Python doesn’t recognize that as valid. 
#The only answer I can really give is, you just can’t.
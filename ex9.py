# -*- coding: utf-8 -*-
#here's some new strange stuff, remember type it exactly.
#days are put into line
days = "Mon Tue Wed Thu Fri Sat Sun"
#\n puts them on seperate lines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months
#tripple lets you do multiple lines
print """
There's something going on here
With the three double-quotes.
We'll be able to type as much as we like
Even 4 lines if we want, or 5 or 6
"""

#What if I wanted to start the months on a new line?
#You simply start the string with \n like this: "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#Why do the \n newlines not work when I use %r?
#That’s how %r formatting works; it prints it the way you wrote it (or close to it). 
#It’s the “raw” format for debugging.

#Why do I get an error when I put spaces between the three double-quotes?
#You have to type them like """ and not " " ", meaning with no spaces between each one.

#Is it bad that my errors are always spelling mistakes?
#Most programming errors in the beginning (and even later) are simple spelling 
#mistakes, typos, or getting simple things out of order.
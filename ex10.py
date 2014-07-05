# -*- coding: utf-8 -*-
##SUMMARY

#\n (backslash n) between the names of the months. What these two 
#characters do is put a new line characterinto the string at that point.
#use of the \ (backslash) character is a way we can put difficult-to-type 
#characters into a string.
#plenty of these “escape sequences” available for different characters you might 
#want to put in, but there’s a special one, the double backslash, which is just 
#two of them \. These two characters will print just one backslash. We’ll try a 
#few of these sequences so you can see what I mean.

#Another important escape sequence is to escape a single-quote ' or double-quote ". 
#Imagine you have a string that uses double-quotes and you want to put a double-quote 
#in for the output. If you do this "I "understand" joe." then Python will get 
#confused since it will think the " around "understand" actually ends the string. 
#You need a way to tell Python that the " inside the string isn’t a real double-quote.
#To solve this problem, you escape double-quotes and single-quotes so Python 
#knows what to include in the string. Here’s an example:
#"I am 6'2\" tall." # escape double-quote inside string 'I am 6\'2" tall.' 
# escape single-quote inside string
#The second way is by using triple-quotes, which is just """ and works like a 
#string, but you also can put as many lines of text as you want until you type """
#again. We’ll also play with these.

tabby_cat = "\t I'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat= """
I'll do a list:
\t* Cat Food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Escape Sequences

#This is the list of all the escape sequences Python supports. You may not use 
#many of these, but memorize their format and what they do anyway. Also try 
#them out in some strings to see if you can make them work.
#Escape What it does.
#\\ Backslash (\)
#\' Single-quote (') \" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only) \r ASCII carriage return (CR)
#\t ASCII horizontal tab (TAB)
#\uxxxx Character with 16-bit hex value xxxx (Unicode only) \Uxxxxxxxx Character ...
#with 32-bit hex value xxxxxxxx (Unicode only) \v ASCII vertical tab (VT)
#\ooo Character with octal value oo
#\xhh Character with hex value hh


#Common Student Questions

#I still haven’t completely figured out the last exercise. Should I continue?
#Yes, keep going, and instead of stopping, take notes listing things you don’t 
#understand for each exercise. Periodically go through your notes and see if you 
#can figure these things out after you’ve completed more exercises. Sometimes, 
#though, you may need to go back a few exercises and go through them again.

#What makes \\ special compared to the other ones?
#It’s simply the way you would write out one backslash (\) character. Think about why you would need this.

#When I write // or /n it doesn’t work.
#That’s because you are using a forward-slash / and not a backslash \. 
#They are different characters that do very different things.

#When I use a %r format none of the escape sequences work.
#That’s because %r is printing out the raw representation of what you typed, 
#which is going to include the original escape sequences. Use %s instead. 
#Always remember this: %r is for debugging; %s is for displaying.

#I don’t get Study Drills #3. What do you mean by “combine” escapes and formats?
#One of the things I try to get you to understand is that each of these exercises
#can be combined to solve problems. Take what you know about format sequences and 
#write some new code that uses those and the escapes from this exercise.

#What’s better, ''' or """?
#It’s entirely based on style. Go with the ''' (triple-single-quote) style 
#for now, but be ready to use either, depending on what feels best or what 
#everyone else is doing.
#Exercise 13- Parameters, Unpacking, Variables

#will cover one more input method you can use to pass vars into a script
#script being another name for your .py files
#You know how you type python ex13.py to run the ex13.pyfile?
#well the ex13.py part of the command is called the "arguement"
#"What we'll do now is write a script that also accepts arguements"

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#line 1 we have "import"
    #this is how you add features to your script from the python feature set
    #rather then give you all the features at once, python asks what u want 2 use
    #this keeps pgrms small, but also acts as documentation for programmers later who ready your code
    
#"argv" is the "arguement variable
    #a standard name in programming that is found in other lnaguages
    #this var holds arguements you pass to your Python script when you run in

#line 3 "unpacks" argv
    #rather than holding all the arguements, it gets assigned to 4 vars
    #you can work with: script, first, second and third
    #"unpack" is probably the best word 2 describe the function
    #"Take whatever is in argv, unpack it, and assign it to all the vars on the left in order"
    
#HOLD UP! FEATURES HAVE ANOTHER NAME!
    #called them "features" here
        #little things you import to make python program do more
        #but nobody calls them features
        #just a trick 2 avoid jargon
    #features real name is: modules
        #for now on we will be calling these "features" that we import "modules"
        #also called "libraries" by python programmers
        
# RUN
    #$ python ex13.py first 2nd 3rd 
    #The script is called: ex13.py 
    #Your first variable is: first 
    #Your second variable is: 2nd 
    #Your third variable is: 3rd
    
    #$ python ex13.py stuff things that 
    #The script is called: ex13.py 
    #Your first variable is: stuff 
    #Your second variable is: things 
    #Your third variable is: that
    
    #$ python ex13.py apple orange grapefruit 
    #The script is called: ex13.py
    #Your first variable is: apple
    #Your second variable is: orange
    #Your third variable is: grapefruit


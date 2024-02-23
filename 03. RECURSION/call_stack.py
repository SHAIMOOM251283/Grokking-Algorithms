def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

# Call to greet function
greet("John")


# Here's how the call stack works in the code:

#    The initial call is to the greet("John") function.
#    Inside the greet() function:
#        It prints "hello, John!".
#        Then it calls the greet2(name) function with the argument "John".
#    Inside the greet2() function:
#        It prints "how are you, John?".
#    After greet2() finishes, the program returns to the greet() function.
#        It prints "getting ready to say bye...".
#        Then it calls the bye() function.
#    Inside the bye() function:
#        It prints "ok bye!".
#    After bye() finishes, the program returns to where it was called, which is the end of the greet() function.
#    Finally, the program completes execution.

# When the greet2 function is called, the greet function was partially completed. 
# When a function is called from another function, the calling function is paused in a partially completed state. 

# The call stack for the code looks like this:
#1. greet("John")
#2. - greet2("John")
#3. - - (None, since greet2 does not call any other function)
#4. - bye()
#5. - - (None, since bye does not call any other function)
#6. - (None, since greet does not call any other function)

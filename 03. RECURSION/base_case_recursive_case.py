def countdown(i):
    print(i)
    if i <= 0:  # Base case
        return
    else:  # Recursive case
        countdown(i-1)
countdown(5)  # Example call with a starting value of 5


#def countdown(i):
#    if i <= 0:
#        return
#    print(i)
#    countdown(i-1)
#countdown(5)
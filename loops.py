def while_loop():
    i=0
    while i<1000:
            print (i)
            i=i+1

def for_loop():
    dog=0
    for dog in range(10):
        print (dog)
        
        
def forever_loop():
    while 1==1:
        print ("hi")            


# ask the user to input while or for and make it lower case
answer=input("while loop, for loop, or forever loop?")
answer =answer.lower()


# if elif to decide to run while or for function

if answer == "while":
    while_loop()
elif answer == "for":
    for_loop()
        
elif answer == "forever":
    forever_loop()

else:
    print ("you need to put in ether for, while, or forever please restart and try again")
    
    
    
from pickle import STOP
import time
name=input("what is your name?:")
time.sleep(1)
print(f"well hi there {name}")
time.sleep(1)
food=input(f"so {name} what is your favorite food?:")
time.sleep(1)
whatfood=input(f"wow i have never tried {food} can you discribe it?:")
time.sleep(1)
print("wow that sounds good")
time.sleep(1)
age=input(f"so how old are you {name}?:")
time.sleep(1)
print(f"ahhh so you are {age} i am... you know i really dont know!")
time.sleep(1)
next=input(f"so {name} do you want to continue?:")
if next=="yes":
    print("as you wish!!!!")
elif next=="no":
    print(f"alright then have a great day {name}!")
    
else:
    print("im going to assume you want to continue")




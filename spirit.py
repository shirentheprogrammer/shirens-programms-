import time 
a=1

trustq = ["You follow the fox deep into the enchanted woods",
                  "Ahri: my name is Ahri by the way... whats yours?",
                  "you think long and hard but cant seem to remember... anything."," Ahri: silly me i forgot when spirit come here they have no memory if there life as a mortal",
                  "Ahri: all thanks to thresh...",
                    "after the mention of this thresh Ahri walked silently for a long time"
                        ]


exposed = ["suddenly Ahri begins to tremble "]





# A new world
print(" you wake to flowers falling around you, a majestic fox looking at you walks closer!")
time.sleep(3)
print(" unknown fox: you seem scared dont worry ill be your gide through the spirit relm, come now we cant wait around forever!")
time.sleep(3)
trust=input(" you: hm i wonder if i should trust this fox? (yes/no):")

if trust=="yes":
    while(a<6):
        print(trustq[a])
        time.sleep(3)
        a+=1
    
    

    
    q1=input("should you ask her who thresh is?(yes/no):")
    if q1=="yes":
        print(" Ahri: well if you must know... Thresh is an ambitious and restless spirit of the Shadow Isles. Once the custodian of countless arcane secrets, he was undone by a power greater than life or death, and now sustains himself by tormenting and breaking others with slow, excruciating inventiveness. His victims suffer far beyond their brief mortal coil as Thresh wreaks agony upon their souls, imprisoning them in his unholy lantern to torture for all eternity.")
    time.sleep(20)
        
    if q1=="no":
        print("you dont ask and keep walking")
        print(" Ahri: by the way um stick with me if you dont want thresh well to... you know... torture you for all eternity!")
        















if trust=="no":
    print (" the fox leaves you and thresh harvests your essense and you are traped in his lantern for all of your afterlife!!!!") 


    
    
    
    







#Josephus problem (see online)
#Josephus and comrades surrounded by Roman soldiers and want to avoid capture.
#They do this by systematically killing each other.
#However Josephus prefers capture and wants to ensure he does not die. 
#They decide to arrange themselves in a circle and kill the person standing directly beside them.
#Where should Josephus position himself in the configuration to avoid death?
import math
n = int(input("Input the number of people: "))
k = int(input("Enter the step size: "))

#arrange will use a list to assign people and their alive status as a pair within the list.
def arrange(n):
    circle = []
    
    for i in range(1,n+1):
        person = []
        person.append(i) #indicates the position of the person in the circle
        person.append(1) #we use 1 to indicate they are alive, dead will be indicated by 0
        circle.append(person) #add the person to the circle list

    #print(circle) 
    return circle   

def method2(circle,k): 
    dead = []
    
    round = 0
    while(len(circle)>2):
        alive = []
        i = k
        round+=1
        half = math.floor((len(circle)-1)/2) #ensures we can clear the circle if we need to loop back round with the required person first to go in the next loop round
        while(i+k<=len(circle)+1):
            circle[i-1][1] = 0               #assigns the dead '0' note we need i-1 due to the indexing
            circle[i-1].append(round)        #notes which loop round the circle this person died during
            dead.append(circle[i-1])         #add the dead person to the dead list
            alive.append(circle[i-2])        #add the alive person ie the person directly before the dead person in the circle to the alive list
            i = i + k                        #increases the counter 
            print(i)
        for person in circle:
            #this for loop deletes the dead people froom the circle after each round
            if person[1] == 0:
                index = circle.index(person)
                del circle[index]
                print("Circle after deleting the dead, before reorder: {}".format(circle))
        del circle[:half] #we would have at most half the circle + 1 persons left alive after each round (k=2) so we delete every alive person who has had a turn in this round
        print("Circle with people yet to have a turn: {}".format(circle)) 
        circle = circle + alive #after some rounds ie odd people and even k, the circle will have people who have not had a turn to kill,
                                #this shifts the people who have not killed to the start of the circle for the next round, when necessary        

        print("Dead people after round {} are: {}".format(round,dead))
        print("Alive people after round {} are: {}".format(round,alive))
        print("The rearranged circle after round {} before the start of round {} is : {}".format(round,round+1,circle))

    print("The remaining pair are: {}".format(circle))
    circle.pop(1) #removes the last person to die from the ordered last pair
    print("Final circle is: {}".format(circle))
    return circle[0][0]



people = arrange(n) 
lastman = method2(people,k) 
print("Lastman is at postion: {}".format(lastman))  





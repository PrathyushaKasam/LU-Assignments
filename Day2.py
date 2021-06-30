maxParticipants = int(input("What's the maximum number of lottery tickets do you want to sell?"))
participant=[]
print("Give the names of the participants")
for i in range(0,maxParticipants):
    ele=input()

    participant.append(ele)

import random 
n=random.randint(0,(maxParticipants-1))
print("And The Winner is : " , participant[n] ,"!")
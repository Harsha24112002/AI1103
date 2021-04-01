import random
count=0
testcases=100000
for j in range(1,testcases):
    for i in range(1,testcases):
        throw=random.randint(1,6)
        if throw==5 or throw==6 :
            continue
        if throw ==2:
            count=count+1
            break
        if throw ==1 or throw ==3 or throw ==4:
            break
sim_prob=count/testcases
print("The experimental probability is : ")
print(sim_prob)
print("The calculated probability is : ")
print(0.25)
print("The absolute difference is : ")
print(abs(sim_prob-0.25))
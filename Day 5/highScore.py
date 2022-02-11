scores=input("Enter a list of students scores! ").split()
for i in range(0,len(scores)):
    scores[i]=float(scores[i])

print("the highest score is: "+ str(max(scores)))
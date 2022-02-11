print("Welcome to Tip Calculator")
bill = input("What was the total bill ? \n $")
percentage = input("What percentage tip would you like to give ? 10, 12 or 15 \n")
if(int(percentage) != 10 or int(percentage) != 12 or int(percentage) != 15):
    print("Bill sould be 10 , 12 or 15 %")
    percentage = input("What percentage tip would you like to give ? 10, 12 or 15 \n")
people = input("How many people to split the bill? \n")
sbill= round((float(bill)/float(people)) * (1+(float(percentage)/100)),2)
print("Each person should pay  $" +str(sbill))

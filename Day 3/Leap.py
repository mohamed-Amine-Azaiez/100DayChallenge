year = int(input("Enter a year: \n"))

if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a Leap Year")
        else:
            print(str(year) + " is Not a Leap Year")
    else:
        print(str(year) + " is a Leap Year")
else:
    print(str(year) + " is Not a Leap Year")
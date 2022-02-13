def prime_checker(number):
    isprime=True
    for i in range(2,number-1):
        if number%i ==0:
            isprime=False
    if isprime:
        print("it's a prime number")
    else:
        print("it's not a prime number")


    

n=int(input("Check this number: "))
prime_checker(number=n)
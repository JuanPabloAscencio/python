number = int(input())

def primeCheck(x):
    prime = True
    for i in range(2,number):
        if str(i)
            x=number%i
            if (x == 0):
                prime = False
                print("not a prime")
                break
        if (prime==True):
            print("it's a prime")
            pass
primeCheck(number)

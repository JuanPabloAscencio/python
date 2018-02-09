number = int(input())
prime = True
for i in range(2,number):
    x=number%i
    if (x == 0):
        prime = False
        break
if (prime==True):
    print("It is a prime")
else:
    print("Not a prime")

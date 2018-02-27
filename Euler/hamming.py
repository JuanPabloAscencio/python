import sys
primes = []
result = []
def generalisedHammingNumbers(k, n):
    # Complete this function
   #create a list of the prime numbers in the range
    for i in range(n+1, k+1,):
        for j in range(2,i):
            x = i%j
            if (x==0):
                isPrime = False
                break
            else:
                isPrime = True
        if (isPrime == True):
            primes.append(i)
#check if they are multiples
    for i in range(1, k+1):
        result.append(i)
        for j in primes:
            if (i%j==0):
                result.remove(i)
                break
    return result
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    result = generalisedHammingNumbers(n, k)
    print(len(result))

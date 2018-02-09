print("Enter fibonacci sequence length")
leng = int(input())
lastValue, currentValue, nextValue = 0, 0, 1
for i in range(leng):
    lastValue = currentValue
    print(currentValue)
    currentValue = nextValue
    nextValue = currentValue + lastValue

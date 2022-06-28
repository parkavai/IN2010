import sys
low = 0
high = 1000
i = 0
while (i != 11):
    x = int((low + high)/2)
    if(sys.stdin == "lower"):
        high = x - 1
    if(sys.stdin== "correct"):
        break 
    if(sys.stdin == "higher"):
        low = x + 1
    i += 1
    print(x)
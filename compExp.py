def compExp(a, b, c):
    h = a if(a>b) else b
    high = c if(c>h) else h
    print(high)
    return high

compExp(2,6.7,5.8)

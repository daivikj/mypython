def compNest(a, b, c):
    if(a>b):
        if(c>a):
            print(str(c) + " is the largest")
        else:
            print(str(a) + " is the largest")
    elif(c>a):
        if(b>c):
            print(str(b) + " is the largest")
        else:
            print(str(c) + " is the largest")
    elif(a>c):
        if(b>a):
            print(str(b) + " is the largest")
        else:
            print(str(a) + " is the largest")
    elif(b>a):
        if(c>b):
            print(str(c) + " is the largest")
        else:
            print(str(b) + " is the largest")
    elif(b>c):
        if(a>b):
            print(str(a) + " is the largest")
        else:
            print(str(b) + " is the largest")
    else:
        if(a>c):
            print(str(a) + " is the largest")
        else:
            print(str(c) + " is the largest")

compNest(2,6,9)

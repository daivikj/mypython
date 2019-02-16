def compBool(a, b, c):
    if((a>b) and (a>c)):
        print(srt(a) + " is the largest")
    if((b>c) and (b>a)):
        print(str(b) + " is the largest")
    if((c>a) and (c>b)):
        print(str(c) + " is the largest")

compBool(2,6,5)

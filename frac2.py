def frac2(tup1, tup2):
    num = (tup1[0] * tup2[1]) + (tup1[1] * tup2[0])
    den = tup1[1] * tup2[1]
    return(num , den)

[num, den] = frac2((5, 3),(7, 6))
print(str(num) + '/' + str(den))

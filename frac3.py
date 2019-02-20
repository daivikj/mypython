def frac3(lst1, lst2):
    num = (lst1[0] * lst2[1]) + (lst1[1] * lst2[0])
    den = lst1[1] * lst2[1]
    return(num , den)

[num, den] = frac3([5, 3],[7, 6])
print(str(num) + '/' + str(den))

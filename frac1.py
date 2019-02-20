def addFrac(num1, den1, num2, den2):
    num = (num1 * den2) + (num2 * den1)
    den = den1 * den2
    return(num, den)

(num, den) = addFrac(5, 2, 6, 7)
print(str(num) + '/' + str(den))

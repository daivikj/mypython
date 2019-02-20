def frac4(d1, d2):
    num = (d1['num'] * d2['den']) + (d2['num'] * d1['den'])
    den = d1['den'] * d2['den']
    return (num, den)
(num, den) = frac4({'num' : 5, 'den' : 3}, {'num' : 11, 'den' : 2})
print(str(num) + '/' + str(den))

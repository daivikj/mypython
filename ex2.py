inp = input('Enter your name: ')
print('Hello '+ inp)

hrs = input('Enter hours: ')
rate = input('Enter rate: ')
print(eval(hrs) * eval(rate))

width = 17
height = 12.0
one = width//2
two = width/2.0
three = height/3
four = 1 + 2 * 5
print('Value of width//2 is: '+ str(one) +' Type is: '+ str(type(one)))
print('Value of width/2.0 is: '+ str(two) +' Type is: '+ str(type(two)))
print('Value of height/3 is: '+ str(three) +' Type is: '+ str(type(three)))
print('Value of 1 + 2 * 5 is: '+ str(four) +' Type is: '+ str(type(four)))

cel = float(input('Enter the temp in celsius: '))
fahr = (cel * (9/5)) + 32
print('Temp in fahr is: '+ str(fahr))

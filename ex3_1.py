def pay(hrs, rate):
    rate *= 1.5
    pay = rate * hrs
    return pay

def enter():
    try:
        hrs = input("Enter hours: ")
        rate = input("Enter rate: ")
        p = pay(eval(hrs), eval(rate))
        print('Pay: '+ str(p))

    except:
        print('Please enter a numeric value')
        exit(0)
    
    return

enter()

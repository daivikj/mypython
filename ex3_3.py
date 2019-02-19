def grade(marks):
    if marks>1.0 and marks<0.0:
        g = 'Enter between 0 and 1'
    if marks>=0.9:
        g = 'A'
    elif marks>=0.8:
        g = 'B'
    elif marks>=0.7:
        g = 'C'
    elif marks>=0.6:
        g = 'D'
    elif marks<0.6:
        g = 'F'
        
    return g

def enter():
    try:
        marks = input("Enter marks: ")
        g = grade(eval(marks))
        print('grade: '+ g)

    except:
        print('Please enter a numeric value')
        exit(0)
    
    return

enter()

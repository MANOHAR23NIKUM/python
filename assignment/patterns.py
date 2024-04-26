def half_pyramid():
    num = int(input('enter the number the rows :'))    
    for i in range(num):
        for j in range(0,i+1):
            print('*',end=" ")
        print('\r')

def inverted_pyramid():
    num = int(input('enter the number the rows : '))
    for i in range(num):
        for j in range(num-i):
            print('*',end=" ")
        print('\r') 

def simple_pattern():
    num = int(input('enter the number the rows :'))
    for i in range(num):
        for j in range(num):
            print('*',end=" ")
        print('\r')

def CheckPrime(no):
    i = 0
    Flag = True
    for i in range(2,int(no/2)+1):
        if(no % i == 0):
            Flag = False
            break
    return Flag

# def Sum(A,B):
#     return A+B
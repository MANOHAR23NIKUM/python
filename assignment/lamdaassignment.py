#1) write a progarm which contains one lamda function which accepts one parameter and 
# # return power of two

# Power = lambda A : 2 ** A

# num = int(input('enter the number :'))

# result = Power(num)
# print('power of : ' , result)


#2) write a progaram which contains one lambda function which accept two paramters & return its 
#multiplication .

# Multiplication = lambda A , B : A*B

# num1 = int(input('enter the fisrt number :'))
# num2 = int(input('enter the second number : '))

# result = Multiplication(num1,num2)
# print('multipliction =:',result)


#3) write a program which contains filter(),map()and reduce().
# list contains the number which are accepted
# from user
# filter should filter out all such number which greater than or equal to 70 and less tahn or 
# equal to 90
#map function will incrase each number by 10 reduce with return of all that number

# ex : = [4,34,76,,68,24,89,23,86]
# list after filteration = [76,89,86]
# list after mapping = [86,99,96]
#reduce = 86x90x96

# check_num = lambda No:(No>=70 and No<=90)

# increment = lambda No : No+10

# from functools import reduce
# product = lambda No1,No2 : No1*No2

# def main():
#     print('Enter the size of list:')
#     size = int(input())
#     Data_Input =[]
#     print("Enter the values:")
#     for i in range(size):
#         value = int(input())
#         Data_Input.append(value)
#     print("User List:",Data_Input)

#     Data_filter = list(filter(check_num,Data_Input))
#     print("Filteration:",Data_filter)

#     Data_map = list(map(increment,Data_filter))
#     print('Mapping:',Data_map)

#     Data_reduce = (reduce(product,Data_map))
#     print('Reduce:',Data_reduce)

# if __name__=="__main__":
#     main()



# 4)Write a program which contains filter( ),map( ) and reduce( ) in it.
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such prime numbers
# Map function will multiply each number by 2.
# Reduce will return maximum number from that numers.
# (also solve this same question using lambda function)



def CheckPrime(no):
    i = 0
    Flag = True
    for i in range(2,int(no/2)+1):
        if(no % i == 0):
            Flag = False
            break
    return Flag

def main():
    print('Enter the size of list:')
    size = int(input())
    Data_Input =[]
    print("Enter the values:")
    for i in range(size):
        value = int(input())
        Data_Input.append(value)
    print("User List:",Data_Input)

    Data_filter = list(filter(CheckPrime,Data_Input))
    print("filter prime number :",Data_filter)


if __name__=="__main__":
    main()
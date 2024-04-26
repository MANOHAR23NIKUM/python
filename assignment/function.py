# 1) Write a program which contains one function names as 
# Check_Num ( ) which accept one parameter as number. If 
# number is even then it should display “Even Number” 
# otherwise display “Odd number”

# def Check_Num():
#     num = int(input('enter the number:'))
#     if (num%2 == 0):
#         print('even number')
#     else:
#         print('odd number')

# def main():
#     Check_Num()  

# if __name__=="__main__":  
#     main()

# 2) Create on module named ad Arithmetic which contains 4 
# functions as Add() for addition, Sub() for Subtraction,  
# Mult() for multiplication and Div() for division. All functions 
# accepts two parameters as number and perform operation. 
# Write on python program which call all the functions from 
# Arithmetic module by accepting the parameters from user


# import arithmatic
# print('1.addition\n2.subtraction\n3.multiplication\n4.division')
# select = int(input('seclect 1/2/3/4'))
# print(select)

# def main():
#     number_o1 = int(input('enter first number'))
#     number_02 = int(input('enter the second number'))
#     if (select == 1):
#         ans = arithmatic.addition(number_01,number_02)
#         print(f'{number_01} and {number_02} addition is :',ans)
#     elif (select ==2):
#         ans = arithmatic.subtraction(number_01,number_02)
#         print(f'{number_01} and {number_02} subtraction is :',ans)
#     elif (select == 3):
#         ans = arithmatic.multiplication(number_01,number_02)
#         print(f'{number_01} and {number_02} multiplication is :',ans)
#     elif (select == 4):
#         ans = arithmatic.division(number_01,number_02)
#         print(f'{number_01} and {number_02} division is :',ans)
#     else:
#         print('choose 1/2/3/4')


# if __name__=="__main__":
#     main() 


# 3)Write a program which accept one number from user and     
# check whether number is prime or not 
# Input:5                   
# Output: Prime number 

# def num():
#     num = int(input("Enter a number: "))
#     if(num>1):
#         for i in range(2,num):
#             if((num%i)==0):
#                 print(num,'is not a prime number')
#                 break
#         else:
#             print(num,'is a prime')
#     else:
#         print(num,'is not a prime number')
# def main():
#     num()

# if __name__=="__main__":
#     main()


# without user

# def prime(num):
#     if(num>1):
#         for i in range(2,num):
#             if((num%i)==0):
#                 print(num,'is not a prime number')
#                 break
#         else:
#             print(num,'is a prime')
#     else:
#         print(num,'is not a prime number')
# prime(6) 

# # 4)Write a program which accept N numbers from user and store 
# # it into List. Return Addition of all elements from that List. 
# # Input:Number of elements:8 
# # Enter value : 11  13  14   56   57   58   12   19 
# # Output : Addition of the given list : 240


# def list_addition(data):
#     ans = 0
#     i = 0
#     while(i<len(data)):
#         ans = ans+data[i]
#         i = i+1
#     return ans

# def main():
#     size = int(input('enter the size of list:'))
#     data_input = []
#     print('enter the value:')
#     for i in range(size):
#         value = int(input())
#         data_input.append(value)
#     print('enter value list:',data_input)
#     output = list_addition(data_input)
#     print('addition of list:',output)

# if __name__=="__main__":
#     main()

# 5)Write a program which accept N numbers from user and store it 
# into List. Return Maximum number from that List. 
# Input:  
# Number of elements:8 
# Enter value : 11  13  14   56   57   58   12   19 
# # Output : Maximum Number of the given list : 58 
# def list_addition(data):
#     ans = 0
#     i = 0
#     while(i<len(data)):
#         ans = ans+data[i]
#         i = i+1
#     return ans
# def main():
#     size = int(input('enter the size of list:'))
#     list_input = []
#     print('enter the value:')
#     for i in range(size):
#         value = int(input())
#         list_input.append(value)      
#         print("maximum list:",max(list_input))

# if __name__=="__main__":
#     main()



# 6)Write a program which accept N numbers from user and store it 
# into List. Return Minimum number from that List. 
# Input:  
# Number of elements:8 
# Enter value : 11  13  14   56   57   58   12   19 
# Output : Minimum Number of the given list : 11 

# list =[]
# num =int(input("Enter of Element:"))
# for i in range(num):
#     value=int(input("Enter Element:"))
#     list.append(value)
# min=list[0]
# for i in range(num):
#     if(list[i]<min):
#        min=list[i]
# print("\nMinimum Number is:",min)
# print()

# 7) Write a program which accept N numbers from user and store 
# it into List. Return frequency of that number from that List. 
# Input:  
# Number of elements: 11 
# Enter value : 13    5    4    2    5    7   8    9    5   10   5  
# Element to search: 5 
# Output: 4 

# def main():
#     size = int(input('enter the number'))
#     list_input = []
#     print('enter the value:')
#     for i in range(size):
#         value = int(input())
#         list_input.append(value)
#     num = int(input("enter number to find frequency:"))
#     count = 0
#     for i in range(size):
#        if(list_input[i]==num):
#             count=count+1
#         print("frequency:",count)

# if __name__=="__main__":
#     main()
 

# 8)Write a program which accept N numbers from user and store it 
# into list. Return addition of all prime numbers from that list. 
# Main python file accepts N numbers from user and pass each 
# Number to Check_Prime( ) function which is part of our user 
# defined module named as NumPrime . Name of the function from 
# main python file should be ListPrime(). 
# Input: Number of elements :10 
# Input Elements: 13   12   5    6    8   7   10   2   5   6 

from prime import CheckPrime
def listprime(numbers):
    primeNumber = []
    for Num in numbers:
        if (Num==0 or Num == 1):
            continue
        ret = CheckPrime(Num)
        if(ret == True):
            primeNumber.append(Num)
    return primeNumber

def main():
    print('enter the number of elements:')
    size = int(input())

    data_input = []

    print('enter data:')


    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('list :',data_input)
    list_of_prime = listprime(data_input)
    print('list of the given prime:',list_of_prime)

if __name__=="__main__":
    main()






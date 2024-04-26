# write a program which will display n even number from user
# def checkeven(no):
#     if (no<=0):
#         return 0
#     if not (no%2==0):
#         return checkeven(no-1)
#     else:
#         return no+ checkeven(no-2)
# print('sum of even :',checkeven(6))



# write a program which will give sum of n even numbers
# def sum_of_even(no):
#     if (no == 2):
#         return 2

#     else:
#         return no+ sum_of_even(no-2)
# print('sum of even :',sum_of_even(6))


# write a program which will revers the n even number
def sum_of_even(n):
    if(n==2):
        return  2
    else:
        return n-sum_of_even(n+2)
print('sum of even:',sum_of_even(6))

# write a program which will reverse the string
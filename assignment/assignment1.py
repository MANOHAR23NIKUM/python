# 1) write a program that accepts the name of the person and display it as given below

name = input('what is your name?')
print('my name is:',name)  


# 2) create tip calculator
    # user please enter total bill(new line)amount rs.
    # user: how much % tips would you like to give? 10 15 or 20?
    # user : how many people to split the bill
    ## total bill amount Rs.4500.45
    ## split bill = 4
    ## each person should pay Rs.1237.62 (hint use round function)

bill = float(input("what was the total bill? Rs"))
print("total bill:",bill)

tip = int(input("how mucch tip would you like to give? 10, 15, or 20?"))
print("tip given:",tip)

people = int(input("how many people to split the bill?"))
print("split the bill:",people)
tip



# 3) expected output
# enter value : shreya
# enter value shreya and its <class 'str'>

# enter value: 23
# enter value 23 and its <class 'str'>

# enter value :23
# enter value 23 and its <class 'int'>

# enter value : 23.4
# enter value 23.4 and its <class 'float'>

value_01 = input('Enter value:')
print(f"Enter value {value_01}",value_01,type(value_01))

value_02 = input('Enter value:')
print(f"Enter value",value_02,type(value_02))

value_03 = int(input('Enter value:'))
print(f"Enter value",value_03,type(value_03))

value_04 = float(input('Enter value:'))
print(f"Enter value",value_04,type(value_04))

# 4) write a program which accep two numbers from user
     # enter the first number : 6
     # enter the second number : 7

print("enter first number:",end='')
number_01 = int(input())
print("type of number 1",type(number_01))
print("enter second number:",end='')
number_02 = int(input())
print(f"addition:",number_01 + number_02 )
print(f"subtraction:",number_01 - number_02)
print(f"floor division:",number_01// number_02)
print(f"multiplication:",number_01 * number_02)

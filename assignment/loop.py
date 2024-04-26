# 1)Write a program to print the following using while loop
# - First 10 even numbers 
# - First 10 odd numbers 
# - First 10 natural numbers
# - First 10 whole numbers 
print()
count = 0 
while(count<=20):
    count += 2
    print(count)


print()
count = 1
while(count<=20):
    count += 2
    print(count)

count = 0
while(count <=10):
    count += 1
    print(count)

count = 0
while (count <=10):
    count +=1
    print(count)

#2)Write a program to print first 10 natural number in reverse order using while loop 

count = 10
while (count > 0):                
    count = count -1
    print(c )

# 3) Write a program to print sum of first 10 Natural numbers 
sum = 0
for i in range(1,11):
    print(i)                  
    sum += i
    print(sum)
        
# 4) Write a program to print sum of first 10 Even Numbers 
sum = 0
for i in range(1,11):
    if i%2 == 0:
        print("is even number:",i)
        sum += i
        print(sum)
    
# 5) Write a program to print table of a number entered from the user 

num = int(input('Enter a number: '))     
count = 1         
print ("The Multiplication Table of:",num)    
while (count <= 10):    
    num = num * 1    
    print(num * count)    
    count +=1
print()


# 6) Write a program to print first 10 integers and their squares using while loop 

i = 0
while (i<= 10):
    i=i+1
    print('square of integer:',i*i)


# 7) Write a program to print first 10 natural number in reverse order using while loop
count = 10
while (count > 0):                
    count = count -1
    print(count)


# 9)Write a program to find the sum of the digits of a number accepted from the user

i = int(input("enter number to find sum of the digits:"))
sum = 0
while (i>0):
    sum = sum+i%10
    i=i//10
    print("sum of digits:",sum)

print("-"*50)

# 10) Write a program to find the product of the digits of a number accepted from the user
i = int(input("enter number "))
prod = 1
while (i>0):
    prod = prod*(i%10)
    i=i//10
    print("product of digits:",prod)

print("-"*50)


# 11) Write a program to reverse the number accepted from user using while loop
i = int(input("enter the number"))
while (i > 0):                
    i = i -1
    print(i)
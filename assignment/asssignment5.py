# 1)Write a program which will swap the two numbers without using third 
# variable? 

def swap_numbers(a, b):
    print("a =", a)
    print("b =", b)
    a = a + b
    b = a - b
    a = a - b

    print("a =", a)
    print("b =", b)

num1 = 10
num2 = 20
swap_numbers(num1, num2)


# 2)Write a program which will swap the two numbers with using third 
# variable? 

def numbers(a, b):
    print("a =", a)
    print("b =", b)

    ans = a
    a = b
    b = ans

    print("a =", a)
    print("b =", b)

num1 = 10
num2 = 20
numbers(num1, num2)

 
# 3)Write a program to check whether a number entered is a three-digit number 
# or not. 
# Example: 
# Input: Enter the number: 12 
# Output: Not a three-digit number 


def check_three_digit_number(number):

    if 100 <= number <= 999:
        return True
    else:
        return False

number = int(input("Enter the number: "))

if check_three_digit_number(number):
    print("It's a three-digit number")
else:
    print("Not a three-digit number")



# 4)Write a program for checking whether a character is a vowel or consonant 
# Example: 
# Input: Enter the character: u 
# Output: Given character is a vowel 

def check(no):
    if no in ['v', 'o', 'w', 'e', 'l']:
        return " character is a vowel"
    else:
        return " character is a consonant"

character = input("Enter the character: ")

print(check(character))


# 5)Write a program to count vowels or consonants of the given string 
# Example: 
# Input: Enter the string: Python 
# Output: The number of vowels: 1 
# The number of consonants: 5 

def check():
    c = input('enter the string : ')
    vowel = 0
    consonant = 0
    
    for i in range(0,len(c)):
        if(c[i]!=''):
            if(c[i]=='a' or c[i]=='e' or c[i]=='p' or c[i]=='y' or c[i]=='t' or c[i]=='h' or c[i]=='o' or c[i]=='n' or c[i]=='z'):
                vowel = vowel+1

            else:
                consonant = consonant+1
        print('number of vowels :',vowel)
        print('number of consonants :',consonant)

def main():
    check()

if __name__=="__main__":
    main()


# 6)Write a Python program that accepts a word from the user and reverses it 
# Example: 
# Input: Enter the word: python 
# Output: nohtyp

# using slicing

character = input('enter the word :')
print(character[-1::-1])

# using for lopp

word = input('enter the word :')
for i in range((len(word)-1),-1,-1):
    print(word[i],end='')


# 7)Write a program to find the last digit in a number 
# Input: Enter the number:123456 
# Output: The last digit in a given number 123456 = 6


number  = int(input('enter the number :'))

last_digit = number % 10

print('The last digit is :',last_digit)
#### menu card using dictionary

# def menu_card():
#     fruits = {'fruit1':'mango','fruit2':'banana','fruit3':'apple'}
#     print('1.display\n 2.add\n 3.remove')
#     select = int(input('enter the number :'))
#     print(select)
#     if (select == 1):
#         print('display item:',fruits)
#     elif (select == 2):
#         update_method =fruits.update({'fruit4':'chiku'})
#         print('add item:',fruits)
#     elif (select == 3):
#         pop_method = fruits.pop('fruit1')
#         print('remove item you want item:',fruits)
#     else:
#         print('choose 1/2/3')
# def main():
#     menu_card()    

# if __name__=="__main__":  
#     main()  


### ATM program

# def ATM():
#     print('Display\n 1.Pin\n 2.pin genrate\n 3.withdraw\n 4.balance')
#     choose = int(input('select the number:'))
#     pin=(1234)
#     amount=(4000)
#     balance=(5000)
#     if (choose==1):
#         while True:
#             entered_pin = int(input('enter the pin:'))
#             if entered_pin == pin:
#                 print('pin verified')
#                 break
#             else:
#                 print('wrong pin')
#                 break

#     elif (choose==2):
#         create_pin = int(input('enter the pin you want:'))
#         print('your new pin:',create_pin)

#     elif(choose==3):
#         while True:
#             withdraw_amount = int(input('enter the amount you want:'))
#             if withdraw_amount == amount:
#                 print('collect the cash')
#                 break
#             else:
#                 print('Insufficient balance')
#                 break

#     elif (choose==4):
#         print('your balance is 5000:')

#     else:
#         print('error')
          


# def main():
#     ATM()
    
# if __name__=="__main__":
#     main()


# 3) calculater using dictionary

# def main():
#     def Addition(n1, n2):
#         return n1 + n2
#     def Subtraction(n1, n2):
#         return n1 - n2
#     def Multiplication(n1, n2):
#         return n1 * n2
#     def Division(n1, n2):
#         return n1/n2
#     def Modulus(n1,n2):
#         return n1%n2
#     def Exponentiation(n1,n2):
#         return n1**n2
#     def FloorDivision(n1,n2):
#         return n1//n2
        
#     operation = str(input("Pick an operation: \n +addition \n -ubtraction \n *multiplication \n /Division \n %Modulus \n **Exponentiation \n //FloorDivision "))
#     n1 = int(input(" first number :"))
#     n2 = int(input("second number : \n"))
#     dict = {"+":Addition, "-": Subtraction, "*": Multiplication, "/": Division, "%":Modulus, "**":Exponentiation, "//":FloorDivision}
#     function = dict[operation]
#     result = function(n1,n2)
#     print(f"{n1} {operation}  {n2} : {result}")

# if __name__=="__main__":
#     main()


# 4)  5 questions program


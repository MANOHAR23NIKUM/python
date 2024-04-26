# fruits = ['mango','banana','apple']
#1) def add =enter the fruits you want to add
   #'grapes'
   # grapes add
   #[mango,banana,apple,grapes]
#2) update = enter the fruit you want to add
    # apple
    # replace : pineapple
    #[mango,banana.pineapple,grapes ]
#3) delete = remove banana


def menu():
    fruit = ['mango','pineapple','grapes' ]
    print('1.Display\n 2.addition\n 3.update\n 4.remove')
    option = int(input('enter number :'))
    print(option)
    if (option == 1):
        print('display fruit:',fruit)
    elif (option == 2):
        value =(input('enter fruit:'))
        fruit.append(value)
        print('addition of list:',fruit)
    
    elif (option == 3):
        current_value = input("Enter Current fruit:")
        update_value = input("Enter New fruit:")
        value = fruit.index(current_value)
        fruit[value]=update_value
        print("Fruits Updated Successfully:",fruit)

    elif (option == 4):
        value =(input('enter fruit:'))
        fruit.remove(value)
        print('remove iteam:',fruit)
    else:
        print('select 1/2/3')
def main():
    menu()    

if __name__=="__main__":  
    main()  

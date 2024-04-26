def add_to_cart():
    items = ['bag','shoes','jens','toy']
    print('1.display\n 2.add\n 3.remove\n 4.number of items')
    select = int(input('enter the number :'))
    print(select)
    if (select == 1):
        print('display item:',items)
    elif(select == 2):
        value = input('add the iteam you want')
        items.append(value)
        print('add items:' ,items)
    elif(select == 3):
        value = input('select the item:')
        items.remove(value)
        print('remove the item:',items)
    elif(select == 4):
        value = input('add the iteam:')
        items.append(value)
        items.count(items)
        print('number of items:',items)
def main():
    add_to_cart()    

if __name__=="__main__":  
    main()  

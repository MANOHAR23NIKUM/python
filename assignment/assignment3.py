# 1)Write a program which contains one class named as Demo.
# That class contains one class variable as value
# There are two instance methods of class as Fun and Gun which displays values of instance variables
# Initialise instance variable in constructor by accepting the values from user
# After creating the class create the two objects of Demo class as
# Obj1 =Demo(11,21)
# Obj2 = Demo(51,101)

# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
   
    def Fun(self):
        print("value1:",self.value1)
        print("value2:",self.value2)
        
    def Gun(self):
        print("value1:",self.value1)
        print("value2:",self.value2)
      
def main():
    Obj1 = Demo( 11 , 21)
    Obj1.Fun()
    Obj1.Gun()
    Obj2 = Demo(51,101)
    Obj2.Fun()
    Obj2.Gun()
    
if __name__=="__main__":
    main()

# 2)Write a program which contains one class named as BookStore.
# Bookstore class contains two instance variables as Name , Author.
# That class contains one class variable as NoofBooks which is initialize to 0
# There is one instanace methods of class as Display which displays name, author and number of books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.
# After creating the class create the two objects of BookStore class as
# Obj1=Bookstore(“Linux System Programming”,”Robert Love”)
# Obj1.Display()  # Linux System Programming. No of books : 1

# Obj2=Bookstore(“C Programming”,”Robert Love”)
# Obj2.Display()  # C Programming by Dennis Ritchie. No of books :2

class BookStore:
    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        NoofBooks = 1

    def Display(self):
        print(self.Name)
        print(self.Author)
        
def main():
    obj1 = BookStore('Linux System Programming','Robert Love')
    obj1.Display()

    obj1 = BookStore('C Programming','Robert Love')
    obj1.Display()
   
if __name__=="__main__":
    main()


# 3)Write a program which contains one class named as Circle
# Circle class contains three instance variables as Radius,Area ,Circumference.
# That class contains one class variable as PI which is initialize to 3.14
# Inside init method initialize all instance variables to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
# ,Display( )
# Accept method will accept value of Radius from user.
# CalculateArea () method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference () method will calculate circumference of circle and store it into instance variable 
# Circumference.
# And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
# After designing the above class call all instance methods by creating multiple objects

class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print('Radius of circle:')
        self.Radius =float(input('enter the radius'))

    def CalculateArea(self):
        self.Area = self.PI*(self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Radius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)


def main():
    a = Circle()
    a.Accept()
    a.CalculateArea()
    a.CalculateCircumference()
    a.Display()

if __name__=="__main__":
    main()




# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects

class BankAccount:
    
    ROI = 10.5
    def __init__(self):
        self.Name = ''
        self.Amount = 0

    def CreateAccount(self):
        print('enter your name:')
        self.Name = input()

        print('enter the amount:')
        self.Amount= int(input())

    def Deposit(self):
        self.Amount = int(input('Deposit amount'))

    def Withdraw(self):
        self.Withdraw = int(input('Withdraw amount'))
        ans = self.Withdraw - self.Amount
        return ans

    @classmethod
    def CalculateInterst(cls):
        print('Rate of interest of FD:',cls.ROI)
    
    def Display(self):
        print('name of Account Holder :',self.Name)
        print('Current Amount in account:',self.Amount)

def main():
    BankAccount.CalculateInterst()
    user1 = BankAccount()
    user1.CreateAccount()
    user1.Deposit()
    user1.Withdraw()
    user1.Display()

if __name__=="__main__":
    main()

# 5)Write a program which contains one class named as Numbers.
#  Arithmetic class contains one instance variables as Value.
#  Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.

class Number():
    def __init__(self):
        value = ''

    def Arithmatic(self):
        value = int(input('enter the number : '))

    def ChkPrime(self):     

    





# 6)Write a program which contains one class named as Numbers.
#  Arithmetic class contains one instance variables as Value1,Value2.
#  Inside init method initialize all instance variables to 0.
# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of Value1 and Value2 and return result.
# Subtraction() method will perform subtraction of Value1 and Value2 and return result.
# Multiplication() method will perform multiplication of Value1 and Value2 and return result.
# Division() method will perform division of Value1 and Value2 and return result.
# After Designing the above class call all instance methods by creating multiple objects.


class Numbers():
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input('enter first number :'))
        self.value2 = int(input('enter the second number :'))

    def Addition(self):
        ans = self.value1 + self.value2
        return ans

    def subtraction(self):
        ans = self.value1 - self.value2
        return ans

    def Multiplication(self):
        ans = self.value1 * self.value2
        return ans

    def Division(self):
        ans = self.value1 / self.value2
        return ans

def main():
    obj1 = Numbers()
    obj1.Accept()
    output1 = obj1.Addition()
    print('Addition : ',output1)
    output2 = obj1.subtraction()
    print('subtraction : ',output2)
    output3 = obj1.Multiplication()
    print('Multiplication : ',output3)
    output4 = obj1.Division()
    print('Division : ',output4)

if __name__=="__main__":
    main()


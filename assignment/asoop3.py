class Number:
    def __init__(self):
        self.size = 0
        self.arr = list()
        print(type(self.arr))

    def Accept(self):
        print('enter hoe many elements you want:')
        self.size = int(input())
        print('enter values')
        value = 0
        for i in range(0,self.size):
            value= int(input())
            self.arr.append(value)

    def Display(self):
        print('elements from list are:')
        for i in range(0,self.size):
            print(self.arr[i])

    def Summation(self):
        sum = 0
        for i in range(0,self.size):
            sum = sum + self.arr[i]
        return sum

    def maximum(self):
        max = 0
        for i in range(0,self.size):
            if(self.arr[i]>max):
                max =self.arr [i]
        return max

    def minimum(self):
        min =self.arr[0] 
        for i in range(0,self.size):
            if(self.arr[i]<min):
                min = self.arr [i]
        return min

    def average(self):
        sum = 1
        for i in range(0,self.size):
            if(self.arr[i]+ sum):
                sum = sum / self.arr[i]
        return sum

def main():
    obj = Number()
    obj.Accept()
    obj.Display()
   

    output = obj.Summation()
    print('summation of the elements :',output)
    output1 = obj.maximum()
    print('maximum of the elements:',output1)
    output2 = obj.minimum()
    print('minimum of the elemnts:', output2)
    output3 = obj.average()
    print('average of the elements:',output3)

if __name__=="__main__":
    main()

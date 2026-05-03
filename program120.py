class Logic:
    def DigitSum(Arr, Length):

        Digit = 0
        No = 0

        for i in range(Length):

            Sum = 0
            
            No = Arr[i]

            if No < 0:
                No = -No

            while(No != 0):
                Digit = No % 10

                Sum = Sum + Digit

                No = No // 10

            print(Arr[i],end=" ")
            print("Summation is: ",Sum)    
                    
class program:
    def main():
        Size = int(input("Enter the Number of Element: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Element: "))
            list.append(Num)

        Logic.DigitSum(list, Size)

if __name__ == "__main__":
    program.main()
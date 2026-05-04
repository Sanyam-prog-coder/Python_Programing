class Logic:
    def Difference(Arr, Length):
        SumEven = 0
        SumOdd = 0

        for i in range(Length):
            if(Arr[i] % 2 == 0):
                SumEven = SumEven + Arr[i]
            elif(Arr[i] % 2 != 0):
                SumOdd = SumOdd + Arr[i]

        return SumEven - SumOdd

class program:
    def main():
        Value = int(input("Enter Number: "))

        list = []

        for i in range(Value):
            Num = int(input("Enter Elements: "))
            list.append(Num)

        Result = Logic.Difference(list, Value)

        print(Result)

if __name__ == "__main__":
    program.main()
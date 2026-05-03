class Logic:
    def Difference(Arr, Length):
        Max = Arr[0]
        Min = Arr[0]
        Diff = 0

        for i in range(Length):
            if(Arr[i] < Min):
                Min = Arr[i]

            if(Arr[i] > Max):
                Max = Arr[i]
            
        Diff = Max - Min

        return Diff
            
class program:
    def main():
        Size = int(input("Enter the Number of Element: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Element: "))
            list.append(Num)

        Result = Logic.Difference(list, Size)

        print(Result)        

if __name__ == "__main__":
    program.main()
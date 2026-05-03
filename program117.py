class Logic:
    def Minimum(Arr, Length):
        Min = Arr[0]

        for i in range(Length):
            if(Arr[i] < Min):
                Min = Arr[i]
            
        return Min

class program:
    def main():
        Size = int(input("Enter the Number of Element: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Element: "))
            list.append(Num)

        Result = Logic.Minimum(list, Size)

        print(Result)        

if __name__ == "__main__":
    program.main()
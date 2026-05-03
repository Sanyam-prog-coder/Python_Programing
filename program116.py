class Logic:
    def Maximum(Arr, Length):
        Max = Arr[0]

        for i in range(Length):
            if(Arr[i] > Max):
                Max = Arr[i]
            
        return Max

class program:
    def main():
        Size = int(input("Enter the Number of Element: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Element: "))
            list.append(Num)

        Result = Logic.Maximum(list, Size)

        print(Result)        

if __name__ == "__main__":
    program.main()
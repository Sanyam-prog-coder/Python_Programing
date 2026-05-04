class Logic:
    def Display(Arr, Length):
        
        for i in range(Length):
            if Arr[i] % 5 == 0:
                print(Arr[i])

class program:
    def main():
        Size = int(input("Enter Number of Element: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Elements: "))
            list.append(Num)

        Logic.Display(list, Size)

if __name__ == "__main__":
    program.main()
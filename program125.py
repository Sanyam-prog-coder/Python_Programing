class Logic:
    def Diplay(Arr, Length):
        for i in range(Length):
            if(Arr[i] % 11 == 0):
                print(Arr[i])

class program:
    def main():
        Size = int(input("Enter Number: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Elements: "))
            list.append(Num)

        Logic.Diplay(list, Size)

if __name__ == "__main__":
    program.main()
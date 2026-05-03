class Logic:
    def Digit(Arr, Length):
        
        for i in range(Length):
            if((Arr[i] >= 100 and Arr[i] <= 999) or 
                (Arr[i] >= -999 and Arr[i] <= -100)):
                print(Arr[i])
            
class program:
    def main():
        Size = int(input("Enter the Number of Element: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Element: "))
            list.append(Num)

        Logic.Digit(list, Size)

if __name__ == "__main__":
    program.main()
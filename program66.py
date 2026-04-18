def DispayDigit(No):
    Digit = 0

    if(No < 0):
        No = -No
        
    while No != 0:
        Digit = No % 10

        print(Digit)

        No = No // 10 

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    DispayDigit(Value)

if __name__ == "__main__":
    main()
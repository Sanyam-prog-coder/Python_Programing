def DispayDigit(No):
    Digit = 0
    Freq = 0

    if(No < 0):
        No = -No
        
    while No != 0:
        Digit = No % 10

        if Digit < 6:
            Freq = Freq + 1
        
        No = No // 10

    return Freq
    
def main():
    Value = 0
    iRet = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = DispayDigit(Value)

    print(iRet)

if __name__ == "__main__":
    main()
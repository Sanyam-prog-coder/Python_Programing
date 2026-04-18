def DispayDigit(No):
    Digit = 0

    if(No < 0):
        No = -No
        
    while No != 0:
        Digit = No % 10
        if Digit == 0:
            return True
        
        No = No // 10

        return False
    
def main():
    Value = 0
    bRet = False

    print("Enter Number: ")
    Value = int(input())

    bRet = DispayDigit(Value)

    if(bRet == True):
        print("It contains Zero")
    else:
        print("It not contains Zero")

if __name__ == "__main__":
    main()
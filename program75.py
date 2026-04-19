import math

def MultDigit(No):
    Digit = 0
    Sum = 0
    Sub = 0

    if(No < 0):
        No = -No

    while(No != 0):
        Digit = No % 10

        if(Digit % 2 == 0):
            Sum = Sum + Digit
        else:
            Sub = Sub + Digit
        
        No = math.floor(No / 10)

    return Sum - Sub

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = MultDigit(Value)

    print(iRet)

if __name__ == "__main__":
    main()
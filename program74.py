import math

def MultDigit(No):
    Digit = 0
    Mult = 1

    if(No < 0):
        No = -No

    while(No != 0):
        Digit = No % 10

        Mult = Mult * Digit
        
        No = math.floor(No / 10)

    return Mult

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = MultDigit(Value)

    print(iRet)

if __name__ == "__main__":
    main()
import math

def CountRange(No):
    Digit = 0
    Count = 0

    if(No < 0):
        No = -No

    while(No != 0):
        Digit = No % 10

        if(Digit > 3 and Digit < 7):
            Count = Count + 1
        
        No = math.floor(No / 10)

    return Count

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = CountRange(Value)

    print(iRet)

if __name__ == "__main__":
    main()
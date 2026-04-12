def Factorial(No):
    Frequency = 1

    if(No < 0):
        No = -No

    for i in range(1,No + 1):
        Frequency = Frequency * i

    return Frequency

def main():
    Value = 0
    iRet = 0

    print("Enter Number")
    Value = int(input())

    iRet = Factorial(Value)

    print("Factorial of ",Value,":",iRet)

if __name__ == "__main__":
    main()
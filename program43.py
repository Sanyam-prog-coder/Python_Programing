def EvenFactor(No):
    if(No < 0):
        No = -No

    Fact = 1

    for i in range(1, No):
        if(i % 2 == 0):
            Fact = Fact * i

    return Fact

def main():
    iValue = 0

    print("Enter Number: ")
    iValue = int(input())

    iRet = EvenFactor(iValue)

    print("Even Factorial of Number is : ",iRet)

if __name__ == "__main__":
    main()
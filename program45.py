def Factorial(No):
    if(No < 0):
        No = -No

    EvenFact = 1
    OddFact = 1

    for i in range(1, No):
        if(i % 2 == 0):
            EvenFact = EvenFact * i

    for i in range(1, No +1):
        if(i % 2 != 0):
            OddFact = OddFact* i

    return EvenFact - OddFact

def main():
    iValue = 0

    print("Enter Number: ")
    iValue = int(input())

    iRet = Factorial(iValue)

    print("Factores Diffrence is : ",iRet)

if __name__ == "__main__":
    main()
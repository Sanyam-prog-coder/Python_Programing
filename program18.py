def SumNonFact(iNo):
    
    iSum = 0

    for i in range(1,iNo):
        if(iNo % i != 0):
            iSum = iSum + i

    return iSum

def main():
    iValue = 0
    iRet = 0

    print("Enter Number")
    iValue = int(input())

    iRet = SumNonFact(iValue)

    print("Summation of Non Factors ",iValue, "is:",iRet)

if __name__ == "__main__":
    main()
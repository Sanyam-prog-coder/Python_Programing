def FactDiff(iNo):

    iFact = 0
    iNonFact = 0

    for i in range(1, iNo):
        if(iNo % i == 0):
            iFact = iFact + i
        else:
            iNonFact = iNonFact + i
         
    return iFact - iNonFact

def main():
    iValue = 0
    iRet = 0

    print("Enter Number : ")
    iValue = int(input())

    iRet = FactDiff(iValue)

    print("Difer Between",iRet)

if __name__ == "__main__":
    main()
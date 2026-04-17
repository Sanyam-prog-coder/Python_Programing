def SumEven_Factor(No):

    SumEven = 0

    if(No <= 0):
        print("Invalid Number")
        return
    
    for i in range(1, No):
        if((No % i == 0) and (i % 2 == 0)):
            SumEven = SumEven + i

    return SumEven

def main():
    Value = 0
    iRet = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = SumEven_Factor(Value)

    print(iRet)

if __name__ == "__main__":
    main()
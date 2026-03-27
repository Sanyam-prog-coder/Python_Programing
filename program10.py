def PrintEven(iNo):
    if(iNo <= 0):
        return
    
    iEven = 2

    for i in range(iNo):
        print(iEven,end=" ")
        iEven = iEven + 2
    print()

def main():
    iValue = 0

    print("Enter Nmber :")
    iValue = int(input())

    iRet = PrintEven(iValue)

if __name__ == "__main__":
    main()
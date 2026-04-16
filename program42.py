def DollerToINR(No):
    Doller = 0

    Doller = No * 70

    return Doller

def main():
    iValue = 0

    print("Enter Number in USD: ")
    iValue = int(input())

    iRet = DollerToINR(iValue)

    print("Value of",iValue,"INR is : ",iRet,"$")

if __name__ == "__main__":
    main()
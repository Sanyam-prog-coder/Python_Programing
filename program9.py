def CheckEven(iNo):
    if((iNo % 2) == 0):
        return True
    else:
        return False
    
def main():
    iValue = 0
    bRet = False

    print("Enter Number : ")
    iValue = int(input())

    bRet = CheckEven(iValue)

    if(bRet == True):
        print(iValue,"is Even Number")
    else:
        print(iValue,"is Odd Number")

if __name__ == "__main__":
    main()
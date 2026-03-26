def Division(iNo1, iNo2):
    
    if(iNo2 == 0):
        return
    
    iAns = iNo1 / iNo2

    return iAns

def main():
    iValue1 = 15 
    iValue2 = 5

    iRet = Division(iValue1, iValue2)

    print("Division is : ",iRet)

if __name__ == "__main__":
    main()
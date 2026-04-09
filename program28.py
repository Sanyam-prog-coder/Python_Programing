def CheckEqual(No1, No2):
    if(No1 == No2):
        return True
    else:
        return False

def main():
    Value1 = 0
    Value2 = 0
    bRet = False

    print("Please Enter two Number : ")
    Value1 = int(input())
    Value2 = int(input())

    bRet = CheckEqual(Value1, Value2)
    if(bRet == True):
        print("Equal")
    else:
        print("Not Equal")

if __name__ == "__main__":
    main()
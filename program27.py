def CheckGreater(No):
    if(No > 100):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = False

    print("Please Enter Number")
    Value = int(input())

    bRet = CheckGreater(Value)
    if(bRet == True):
        print("Greater")
    else:
        print("Smaller")

if __name__ == "__main__":
    main()
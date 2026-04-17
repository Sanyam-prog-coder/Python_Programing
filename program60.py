def Divisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = False

    print("Enter Number: ")
    Value = int(input())

    bRet = Divisible(Value)

    if(bRet == True):
        print("Divisiable by 5")
    else:
        print("Not Divisiable by 5")

if __name__ == "__main__":
    main()
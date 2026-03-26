def Check(iNo):
    if((iNo % 5) == 0):
        return True
    else:
        return False

def main():
    iValue = 0

    print("Enter Number : ")
    iValue = int(input())

    bRet = Check(iValue)

    if bRet is True:
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")

if __name__ == "__main__":
    main()
def Display(iNo):
    iCnt = 0

    while(iCnt < iNo):
        print("*")

        iCnt = iCnt + 1

def main():
    iValue = 0

    print("Enter the Number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()
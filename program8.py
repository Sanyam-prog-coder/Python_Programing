def Display(iNo, iFrequency):
    i = 0

    if(iNo < 0 ):
        iNo = iNo

    for i in range(iFrequency):
        print(iNo)


def main():
    iValue = 0
    iCount = 0

    print("Enter First Number : ")
    iValue = int(input())

    print("Enter Frequency : ")
    iCount = int(input())

    Display(iValue, iCount)

if __name__ == "__main__":
    main()
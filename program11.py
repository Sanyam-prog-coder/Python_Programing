def DisplayFactor(iNo):
    if(iNo <= 0):
        iNo = -iNo
    
    for i in range(1,iNo):
        if(iNo % i == 0):
            print(i)

def main():
    iValue = 0

    print("Enter Number : ")
    iValue = int(input())

    DisplayFactor(iValue)

if __name__ == "__main__":
    main()
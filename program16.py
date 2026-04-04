def FactRev(iNo):
    
    for i in range(iNo - 1, 0, -1):
        if(iNo % i == 0):
            print(i)

def main():
    iValue = 0

    print("Enter Number :")
    iValue = int(input())

    FactRev(iValue)

if __name__ == "__main__":
    main()
def Accept(iNo):
    iCnt = 0

    for iCnt in range(iNo):
        print("*")

def main():
    iValue = 0
    
    print("Enter Value to print")
    iValue = int(input())

    Accept(iValue)

if __name__ == "__main__":
    main()
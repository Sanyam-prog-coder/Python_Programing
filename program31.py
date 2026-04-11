def Pattern(No):
    for i in range(No):
        print("$\t*\t",end=" ")

def main():
    iValue = 0

    print("Enter Number")
    iValue = int(input())

    Pattern(iValue)

if __name__ == "__main__":
    main()
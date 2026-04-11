def OddDisplay(No):
    for i in range(1,No + 1):
        if(i % 2 != 0):
            print(i,end=" ")

def main():
    iValue = 0

    print("Enter Number")
    iValue = int(input())

    OddDisplay(iValue)

if __name__ == "__main__":
    main()
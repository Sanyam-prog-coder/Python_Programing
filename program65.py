def Sum_Even_Number(No):
    Sum = 0

    for i in range(1, No + 1):
        if(i % 2 == 0):
            Sum = Sum + i

    return Sum

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = Sum_Even_Number(Value)

    print("Summation of Even Number: ",iRet)

if __name__ == "__main__":
    main()
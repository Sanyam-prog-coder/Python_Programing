def Sum_Factor(No):

    Sum = 0

    if(No <= 0):
        print("Invalid Number")
        return
    
    for i in range(1, No + 1):
        if(No % i == 0):
            Sum = Sum + i

    return Sum

def main():
    Value = 0
    iRet = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = Sum_Factor(Value)

    print(iRet)

if __name__ == "__main__":
    main()
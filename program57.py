def Count_Factor(No):

    Count = 0

    if(No <= 0):
        print("Invalid Number")
        return
    
    for i in range(1, No + 1):
        if(No % i == 0):
            Count = Count + 1

    return Count

def main():
    Value = 0
    iRet = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = Count_Factor(Value)

    print(iRet)

if __name__ == "__main__":
    main()
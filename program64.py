def Sum_Number(No):
    
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum
        
def main():
    Value = 0
    iRet = 0

    print("Enter Number: ")
    Value = int(input())

    iRet = Sum_Number(Value)

    print("Summation od Natural Number: ",iRet)

if __name__ == "__main__":
    main()
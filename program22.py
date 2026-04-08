def FindMax(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    Num1 = 0
    Num2 = 0
    Result = 0

    print("Enter two Number")
    Num1 = int(input())
    Num2 = int(input())

    Result = FindMax(Num1, Num2)

    print("Maximum is :",Result,)

if __name__ == "__main__":
    main()
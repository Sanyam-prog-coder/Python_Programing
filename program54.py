def RangeSumEven(Starting, Ending):
    Sum = 0

    if(Starting > Ending or Starting < 0 or Ending < 0):
        print("Invalid Position")
        return
    
    for i in range(Starting, Ending + 1):
        if(i % 2 == 0):
            Sum = Sum + i

    return Sum

def main():
    Start = 0
    End = 0
    iRet = 0

    print("Enter Starting Point: ")
    Start = int(input())

    print("Enter Ending Point: ")
    End = int(input())

    iRet = RangeSumEven(Start, End)

    print("Summation of Range is:",iRet)

if __name__ == "__main__":
    main()
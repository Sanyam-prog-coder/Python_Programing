def KMtoMeter(No):
    Meter = 0

    Meter = No * 1000

    return Meter

def main():
    Value = 0
    iRet = 0

    print("Enter Distance in KM: ")
    Value = int(input())

    iRet = KMtoMeter(Value)

    print("Distance in meter is : ",iRet)

if __name__ == "__main__":
    main()
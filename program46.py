def CircleAre(Radius):
    Area = 0

    Area = 3.14 * Radius * Radius

    return Area

def main():
    Value = 0
    iRet = 0

    print("Enter Radius: ")
    Value = float(input())

    iRet = CircleAre(Value)

    print("Area of Circle is : ",iRet)

if __name__ == "__main__":
    main()
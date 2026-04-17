def SquareMeter(Value):
    SquareFeet = 0

    SquareFeet = Value * 0.0929

    return SquareFeet

def main():
    Value = 0
    dRet = 0

    print("Enter Area in Square Feet: ")
    Value = int(input())

    dRet = SquareMeter(Value)

    print("Area in Square meter: ",dRet)

if __name__ == "__main__":
    main()
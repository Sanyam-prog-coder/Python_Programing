def ReactArea(width, height):
    Area = 0

    Area = width * height

    return Area

def main():
    Value1 = 0.0 
    Value2 = 0.0
    iRet = 0

    print("Enter Width: ")
    Value1 = float(input())

    print("Enter Height: ")
    Value2 = float(input())

    iRet = ReactArea(Value1, Value2)

    print("Area of Reactangle is: ",iRet)

if __name__ == "__main__":
    main()
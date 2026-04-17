def FHtoCS(Temp):
    Cel = 0.0

    Cel = ((Temp - 32) * (5 / 9))

    return Cel

def main():
    Value = 0.0
    iRet = 0

    print("Enter temprature in Fahrenheit: ")
    Value = float(input())

    iRet = FHtoCS(Value)

    print("Temprature in centigrade: ",iRet)

if __name__ == "__main__":
    main()
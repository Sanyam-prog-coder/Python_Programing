def Percentage(No1, No2):
    percentage = 0.0

    if(No1 == 0):
        print("Total Cannot be a zero")
        return 0.0
    
    percentage = No2 / No1 * 100

    return percentage

def main():
    Value1 = 0
    Value2 = 0
    fRet = 0.0

    print("Please enter total marks")
    Value1 = int(input())

    print("Please enter obtained marks")
    Value2 = int(input())

    fRet = Percentage(Value1, Value2)

    print("Percentage is :",fRet,"%")

if __name__ == "__main__":
    main()
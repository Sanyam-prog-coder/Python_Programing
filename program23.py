def CheckLeapYear(Year):
    if(Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0):
        print(Year,"is a leap year")
    else:
        print(Year,"is not a leap year")

def main():
    Year = 0

    print("Enter Year : ")
    Year = int(input())

    CheckLeapYear(Year)

if __name__ == "__main__":
    main()
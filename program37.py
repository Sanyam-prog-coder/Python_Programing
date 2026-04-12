def Display(No):
    if(No < 0):
        No = -No

    if(No > 9):
        print("Invalid Number")
        return
    
    status = No
    match status:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("Seven")
        case 8:
            print("Eight")
        case 9:
            print("Nine")
        case _:
            print("Invalid Number")

def main():
    Value = 0

    print("Enter Number")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
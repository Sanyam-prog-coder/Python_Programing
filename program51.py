def RangeDisplay(Starting, Ending):
    
    if(Starting > Ending):
        print("Invalid Position")
        return
    
    for i in range(Starting, Ending + 1):
        print(i)

def main():
    Start = 0
    End = 0

    print("Enter Starting Point: ")
    Start = int(input())

    print("Enter Ending Point: ")
    End = int(input())

    RangeDisplay(Start, End)

if __name__ == "__main__":
    main()
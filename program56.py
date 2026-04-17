def Print_Factor(No):
    if(No <= 0):
        print("Invalid Number")
        return
    
    for i in range(1, No + 1):
        if(No % i == 0):
            print(i)

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    Print_Factor(Value)

if __name__ == "__main__":
    main()
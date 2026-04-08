def CheckEvenOdd(No):
    
    if(No % 2 == 0):
        print(No,"Even Number")
    else:
        print(No,"Odd Number")

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    CheckEvenOdd(Value)

if __name__== "__main__":
    main()
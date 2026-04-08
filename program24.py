def CheckNumber(No):
    if(No > 0):
        print(No,"Number is Positive")
    elif(No < 0):
        print(No,"Number is Negative")
    else:
        print(No,"Number is Zero")

def main():
    Number = 0
    
    print("Enter Number")
    Number = int(input())

    CheckNumber(Number)

if __name__ =="__main__":
    main()
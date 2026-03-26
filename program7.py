def Display(iNo):
    if(iNo < 10):
        print("Hello")
    else:
        print("Demo")

def main():
    iValue = 0

    print("Enter Number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()
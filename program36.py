def Number(No):
    if(No < 50):
        print("Small")
    elif(No >= 50 and No <= 100):
        print("Medium")
    else:
        print("Large")

def main():
    Value = 0

    print("Enter Number")
    Value = int(input())

    Number(Value)

if __name__ == "__main__":
    main()
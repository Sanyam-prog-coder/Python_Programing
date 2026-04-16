def Display(No):

    if(No < 0):
        No = -No
        
    for i in range(0, No):
        print("*\t",end=" ")

    for i in range(0, No):
        print("#\t",end=" ")

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
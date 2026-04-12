def Table(No):
    if(No < 0):
        No = -No

    for i in range(No - 1, 10 + 1):
        sum = No * i
        print(sum,end=" ")        

def main():
    Value = 0

    print("Enter Number")
    Value = int(input())

    Table(Value)

if __name__ == "__main__":
    main()
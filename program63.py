def print_Odd_Number(No):
    
    for i in range(1, No + 1):
        if(i % 2 != 0):
            print(i)

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    print_Odd_Number(Value)

if __name__ == "__main__":
    main()
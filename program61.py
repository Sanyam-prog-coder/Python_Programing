def print_Number(No):
    
    for i in range(1, No + 1):
        print(i)

def main():
    Value = 0

    print("Enter Number: ")
    Value = int(input())

    print_Number(Value)

if __name__ == "__main__":
    main()
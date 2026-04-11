def MultipleDisplay(No):
    for i in range(1, 5 + 1):
        print(i * No, end=" ")

def main():
    Value = 0

    print("Enter Number")
    Value = int(input())

    MultipleDisplay(Value)

if __name__ == "__main__":
    main()
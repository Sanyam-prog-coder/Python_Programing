def Pattern(Row, Col):
    for i in range(1,Row + 2):
        for j in range(1,Col + 1):
            print(i,end=" ")
        print()

def main():
    Value1 = int(input("Enter The Row: "))
    Value2 = int(input("Enter The Column: "))

    Pattern(Value1, Value2)

if __name__ == "__main__":
    main()
def Pattern(Row, Col):
    for i in range(Row):
        for j in range(Col):
            print(j + 1,end=" ")
        print()

def main():
    Value1 = int(input("Enter The Row: "))
    Value2 = int(input("Enter The Column: "))

    Pattern(Value1, Value2)

if __name__ == "__main__":
    main()
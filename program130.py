class Logic:
    def Pattern(No):

        for i in range(1, No + 1):
            print(i * 2)

class program:
    def main():
        Value = int(input("Enter Number: "))

        Logic.Pattern(Value)

if __name__ == "__main__":
    program.main()
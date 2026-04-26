class Logic:
    def productOfDigit(No):
        Digit = 0
        Sum = 1

        while(No > 0):
            Digit = No % 10

            Sum = Digit * Sum

            No = No // 10

        print(Sum)

class program:
    def main():
        Value = 0

        print("Enter Number: ")
        Value = int(input())

        Logic.productOfDigit(Value)

if __name__ == "__main__":
    program.main()
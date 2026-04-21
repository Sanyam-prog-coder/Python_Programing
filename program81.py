class Logic:
    def sumOfDigit(No):
        Digit = 0
        Sum = 0

        while(No != 0):
            Digit = No % 10

            Sum = Sum + Digit

            No = No // 10
        
        print(Sum)

class program:
    def main():
        Value = 12345

        Logic.sumOfDigit(Value)

if __name__ == "__main__":
    program.main()
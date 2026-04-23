class Logic:
    def printDigit(No):
        Digit = 0

        while(No != 0):
            Digit = No % 10
            No = No // 10

            print(Digit)


class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())
        
        Logic.printDigit(Value)


if __name__ == "__main__":
    Program.main()
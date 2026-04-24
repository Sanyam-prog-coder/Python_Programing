class Logic:
    def printReverse(No):
        Rev = No

        for i in range(No, 0, -1):
            Rev = i
            print(Rev)


class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())

        Logic.printReverse(Value)

if __name__ == "__main__":
    Program.main()
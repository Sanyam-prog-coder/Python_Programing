class Logic:
    def checkLeapYear(No):
        if(No % 400 == 0) or (No % 4 == 0 and No % 100 != 0):
            print("It is a leap year")
        else:
            print("It is not a leap year")

class Program:
    def main():
        Value = 0

        print("Enter Year: ")
        Value = int(input())

        Logic.checkLeapYear(Value)

if __name__ == "__main__":
    Program.main()
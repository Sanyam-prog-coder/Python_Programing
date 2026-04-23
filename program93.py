class Logic:
    def checkDivisibe(No):
        if No % 5 == 0:
            print(No,"Is Divisible by 5")
        elif No % 11 == 0:
            print(No,"Is Divisible by 11")
        else:
            print(No, "Is not Divisible by 5 or 11")

class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())
        
        Logic.checkDivisibe(Value)


if __name__ == "__main__":
    Program.main()
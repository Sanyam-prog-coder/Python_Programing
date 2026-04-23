class Logic:
    def calculatePower(Base, exp):
        Result = 1

        for i in range(exp):
            Result = Result * Base

        print(Base, "Raised to power",exp, "is: ", Result)
class Program:
    def main():

        print("Enter Base: ")
        Value1 = int(input())

        print("Enter Exp: ")
        Value2 = int(input())
        
        Logic.calculatePower(Value1, Value2)


if __name__ == "__main__":
    Program.main()
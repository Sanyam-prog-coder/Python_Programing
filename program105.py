class Logic:
    def printDivisibleBy2And5(No):

        for i in range(No + 1):
            if(i % 2 == 0 and i % 3 == 0):
                print(i)
            

class program:
    def main():
        Value = 0

        print("Enter Number: ")
        Value = int(input())

        Logic.printDivisibleBy2And5(Value)

if __name__ == "__main__":
    program.main()
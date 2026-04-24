class Logic:
    def sumEvenNumber(No):
        Sum = 0

        for i in range(No):
            if i % 2 == 0:
                Sum = Sum + i

        print(Sum)

class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())

        Logic.sumEvenNumber(Value)

if __name__ == "__main__":
    Program.main()
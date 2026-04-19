class Logic:
    def calculateSum(N):
        Sum = 0

        for i in range(1, N + 1):
            Sum = Sum + i
        
        print(Sum)

class Program:
    def main():
        Value = 10

        Logic.calculateSum(Value)

if __name__ == "__main__":
    Program.main()
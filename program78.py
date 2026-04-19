class Logic:
    def findFactorial(N):
        Fact = 1

        for i in range(1, N + 1):
            Fact = Fact * i

        print(Fact)

class Program:
    def main():
        Value = 5

        Logic.findFactorial(Value)

if __name__ == "__main__":
    Program.main()
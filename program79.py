class Logic:
    def reverseNumber(N):
        Rev = 0

        length = len(str(N))

        for _ in range(length):
            Digit = N % 10

            Rev = Rev * 10 + Digit
            
            N = N // 10

        print(Rev)

class Program:
    def main():
        Value = 1234

        Logic.reverseNumber(Value)

if __name__ == "__main__":
    Program.main()
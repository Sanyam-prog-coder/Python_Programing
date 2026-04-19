class Logic:
    def reverseNumber(N):
        Count = 0

        while(N != 0):
            N = N // 10

            Count = Count + 1

        print(Count)

class Program:
    def main():
        Value = 7654

        Logic.reverseNumber(Value)

if __name__ == "__main__":
    Program.main()
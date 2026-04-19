class Logic:
    def calculateEvenOdd(N):
        
        if(N % 2 == 0):
            print(N," is Even")
        else:
            print(N," is Odd")

class Program:
    def main():
        Value = 7

        Logic.calculateEvenOdd(Value)

if __name__ == "__main__":
    Program.main()
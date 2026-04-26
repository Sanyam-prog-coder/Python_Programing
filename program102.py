class Logic:
    def countEvenOddRange(No):
        Even = 0
        Odd = 0

        for i in range(No):
            if(i % 2 == 0):
                Even = Even + 1
            else:
                Odd = Odd + 1

        print("Even Number Between 1 to ",No,":",Even)
        print("Odd Number Between 1 to ",No,":",Odd)

class program:
    def main():
        Value = 0

        print("Enter Number: ")
        Value = int(input())

        Logic.countEvenOddRange(Value)

if __name__ == "__main__":
    program.main()
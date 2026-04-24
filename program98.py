class Logic:
    def checkPerfect(No):
        Sum = 0

        for i in range(1, No):
            if(No % i == 0):
                Sum = Sum + i

        if(Sum == No and No > 0):
            print(No, ": is Perfect Number")
        else:
            print(No,": is not perfect Number")


class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())

        Logic.checkPerfect(Value)

if __name__ == "__main__":
    Program.main()
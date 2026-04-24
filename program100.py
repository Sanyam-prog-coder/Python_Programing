class Logic:
    def findSmallestNumber(No):
        Digit = 0
        Min = 9

        while(No > 0):
            Digit = No % 10

            if(Digit < Min):
                Min = Digit
            
            No = No // 10

        print(Min)

class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())

        Logic.findSmallestNumber(Value)

if __name__ == "__main__":
    Program.main()
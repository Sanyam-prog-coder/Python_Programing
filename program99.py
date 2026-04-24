class Logic:
    def findLargestNumber(No):
        Digit = 0
        Max = 0

        while(No != 0):
            Digit = No % 10

            if(Digit > Max):
                Max = Digit
            
            No = No // 10

        print(Max)

class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())

        Logic.findLargestNumber(Value)

if __name__ == "__main__":
    Program.main()
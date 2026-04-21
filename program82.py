class Logic:
    def checkPalindrom(No):
        Original = No
        Reverse = 0
        Digit = 0

        while(No != 0):
            Digit = Digit % 10

            Reverse = Reverse * 10 + Digit

            No = No / 10

        if(Original == Reverse):
            print("It is a palindrome Number")
        else:
            print("It is Not a palindrome Number")

class program:
    def main():
        Value = 155

        Logic.checkPalindrom(Value)

if __name__ == "__main__":
    program.main()
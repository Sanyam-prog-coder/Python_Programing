class Logic:
    def sumEvenDigit(No):
         Even = 0
         Odd = 0
         Digit = 0

         while(No != 0):
            Digit = No % 10

            if(Digit % 2 == 0):
                Even = Even + Digit
            else:
                Odd = Odd + Digit

            No = No // 10
    
            print(Even,":",Odd)

class program:
    def main():
        Value = 16792

        Logic.sumEvenDigit(Value)

if __name__ == "__main__":
    program.main()
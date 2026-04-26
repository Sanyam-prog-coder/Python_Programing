class Logic:
    def countFactors(No):

        FactCount = 0

        for i in range(1, No // 2 + 1):
            if(No % i == 0):
                FactCount = FactCount + 1
            
        print(FactCount)

class program:
    def main():
        Value = 0

        print("Enter Number: ")
        Value = int(input())

        Logic.countFactors(Value)

if __name__ == "__main__":
    program.main()
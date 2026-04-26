class Logic:
    def displayFactor(No):
        for i in range(1, No // 2 + 1):
            if(No % i == 0):
                print(i)

class program:
    def main():
        Value = 0

        print("Enter Number: ")
        Value = int(input())

        Logic.displayFactor(Value)

if __name__ == "__main__":
    program.main()
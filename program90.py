class Logic:
    def checkSign(No):
        if(No > 0):
            print(No, "Number is Positive")
        elif(No < 0):
            print(No, "Number is Negetive")
        else:
            print(No,"Number is Zero")

class program:
    def main():
        Value = 8

        Logic.checkSign(Value)

if __name__ == "__main__":
    program.main()
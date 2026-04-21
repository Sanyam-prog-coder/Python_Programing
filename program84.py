class Logic:
    def checkMinimum(A, B):
        if(A < B):
            print(A,"is Minimum")
        elif(B < A):
            print(B,"is Minimum")
        else:
            print("Same Number")

class program:
    def main():
        Value1 = 11
        Value2 = 15

        Logic.checkMinimum(Value1, Value2)

if __name__ == "__main__":
    program.main()
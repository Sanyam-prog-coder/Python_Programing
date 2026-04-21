class Logic:
    def checkMaximum(A, B):
        if(A > B):
            print(A,"is Maximum")
        elif(B > A):
            print(B,"is Maximum")
        else:
            print("Same Number")

class program:
    def main():
        Value1 = 11
        Value2 = 15

        Logic.checkMaximum(Value1, Value2)

if __name__ == "__main__":
    program.main()
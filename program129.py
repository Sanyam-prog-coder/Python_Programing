class Logic:
    def Pattern(No):

        Num = 1

        for i in range(1,No + 1):
            print("#","\t",Num,"\t","*","\t",end=" ")
            Num = Num + 1

class program:
    def main():
        Value = int(input("Enter Number: "))

        Logic.Pattern(Value)

if __name__ == "__main__":
    program.main()
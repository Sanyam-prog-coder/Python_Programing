class Logic:
    def printEvenNumber(No):
        for i in range(1, No + 1):
            if(i % 2 == 0):
                print(i)        

class program:
    def main():
        Value = 20

        Logic.printEvenNumber(Value)

if __name__ == "__main__":
    program.main()
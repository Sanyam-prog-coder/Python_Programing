class Logic:
    def Pattern(No):
        
        cnt = ord('A')

        for i in range(No):
            print(chr(cnt), end="\t")
            cnt = cnt + 1

class program:
    def main():
        Value = int(input("Enter Number: "))

        Logic.Pattern(Value)

if __name__ == "__main__":
    program.main()
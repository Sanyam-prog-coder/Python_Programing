class Logic:
    def displayGrade(No):
        if No < 0 or No > 100:
            print("Invalid Marks")
            return
        
        if No <= 35:
            print("Fail")
        elif No <= 40:
            print("E")
        elif No <= 50:
            print("D")
        elif No <= 60:
            print("C")
        elif No <= 70:
            print("C+")
        elif No <= 80:
            print("B")
        elif No <= 85:
            print("B++")
        elif No <= 90:
            print("A")
        elif No <= 95:
            print("A+")
        else:
            print("A++")


class Program:
    def main():

        print("Enter Number: ")
        Value = int(input())
        
        Logic.displayGrade(Value)


if __name__ == "__main__":
    Program.main()
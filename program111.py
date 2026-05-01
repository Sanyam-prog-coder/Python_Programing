class Logic:
    def Check(arr, No):

        for num in arr:
            if num == No:
                return True
        return False

class program:
    def main():
        Size = int(input("Enter the Number of Element: "))
        Value = int(input("Enter Number: "))

        list = []

        for i in range(Size):
            num = int(input("Enter Elements: "))
            list.append(num)
        
        result = Logic.Check(list, Value)

        if result == True:
            print("true")
        else:
            print("False")

if __name__ == "__main__":
    program.main()
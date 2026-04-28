class Logic:
    def countEven(Arr):
        count = 0

        for num in Arr:
            if num % 2 == 0:
                count = count + 1
            
        return count

class program:
    def main():
        Size = 0
        iRet = 0

        Size = int(input("Enter number of element: "))

        element = []

        for i in range(Size):
            Num = int(input(f"Enter element {i + 1}: "))
            element.append(Num)

        iRet = Logic.countEven(element)

        print("Output: ",iRet)

if __name__ == "__main__":
    program.main()
import gc

class Logic:
    def frequncy(Arr, No):
        count = 0

        for num in Arr:
            if num == No:
                count = count + 1

        return count

class program:
    def main():
        Size = 0
        iRet = 0
        No = 0

        Size = int(input("Enter number of element: "))
        No = int(input("Enter the number: "))

        element = []

        for i in range(Size):
            Num = int(input(f"Enter element {i + 1}: "))
            element.append(Num)

        iRet = Logic.frequncy(element, No)

        print("Output: ",iRet)

        gc.collect()

if __name__ == "__main__":
    program.main()
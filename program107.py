import gc

class Logic:
    def frequncy(Arr):
        countEven = 0
        countOdd = 0

        for num in Arr:
            if num % 2 == 0:
                countEven = countEven + 1
            elif num % 2 == 1:
                countOdd = countOdd + 1
            
        return countEven - countOdd

class program:
    def main():
        Size = 0
        iRet = 0

        Size = int(input("Enter number of element: "))

        element = []

        for i in range(Size):
            Num = int(input(f"Enter element {i + 1}: "))
            element.append(Num)

        iRet = Logic.frequncy(element)

        print("Output: ",iRet)

        gc.collect()

if __name__ == "__main__":
    program.main()
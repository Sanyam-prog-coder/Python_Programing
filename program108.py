import gc

class Logic:
    def check(Arr):

        for num in Arr:
            if num == 11:
                return True
            
        return False

class program:
    def main():
        Size = 0
        iRet = False

        Size = int(input("Enter number of element: "))

        element = []

        for i in range(Size):
            Num = int(input(f"Enter element {i + 1}: "))
            element.append(Num)

        iRet = Logic.check(element)

        if iRet == True:
            print("11 is Present")
        else:
            print("11 is Absent")

        gc.collect()

if __name__ == "__main__":
    program.main()
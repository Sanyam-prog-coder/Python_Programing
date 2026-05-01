class Logic:
    def Product(arr, Length):
        Mult = 1
        Odd = 0
        
        for i in range(Length):
            if(arr[i] % 2 != 0):
                Mult = Mult * arr[i]
                Odd = 1
        
        if Odd == 0:
            return 0
        
        return Mult

class program:
    def main():
        Size = int(input("Enter the Number of Elements: "))

        list = []

        for i in range(Size):
            num = int(input("Enter element: "))
            list.append(num)

        result = Logic.Product(list, Size)

        print(result)

if __name__ == "__main__":
    program.main()
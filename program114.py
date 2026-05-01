class Logic:
    def Range(arr, Legnth, Src, End):
        for i in range(Legnth):
            if arr[i] >= Src and arr[i] <= End:
                print(arr[i])

class program:
    def main():
        Size = int(input("Enter the number of element: "))
        Start = int(input("Enter Start Range: "))
        End = int(input("Enter End Range: "))

        list = []

        for i in range(Size):
            num = int(input("Enter elements: "))
            list.append(num)
        
        result = Logic.Range(list, Size, Start, End)

if __name__ == "__main__":
    program.main()
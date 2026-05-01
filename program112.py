class Logic:
    def firstOcc(arr, Length, No):
        
        for i in range(Length):
            if arr[i] == No:
                return i
        return -1

class program:
    def main():
        Size = int(input("Enter Number of Elemnts: "))
        Value = int(input("Enter Number: "))

        list = []

        for i in range(Size):
            Num = int(input("Enter Elements: "))
            list.append(Num)

        result = Logic.firstOcc(list, Size, Value)

        if result == -1:
            print("There is no such number")
        else:
            print("First Occurance of number is: ",result + 1)

if __name__ == "__main__":
    program.main()
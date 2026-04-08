def FindLargest(X,Y,Z):
    if(X > Y > Z):
        return X
    elif(Y > Z):
        return Y
    else:
        return Z

def main():
    A = 0
    B = 0
    C = 0
    Result = 0

    print("Enter Number")
    A = int(input())
    B = int(input())
    C = int(input())

    Result = FindLargest(A, B, C)

    print("Largest Number is :",Result)

if __name__ == "__main__":
    main()
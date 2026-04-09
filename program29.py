def Multiply(A, B, C):
    iAns = 1

    if(A == 0 and B == 0 and C == 0):
        return 0
    
    if(A != 0):
        iAns = iAns * A
    
    if(B != 0):
        iAns = iAns * B
    
    if(C != 0):
        iAns = iAns * C

    return iAns

def main():
    Value1 = 0
    Value2 = 0
    Value3 = 0
    iRet = 0

    print("Enter Three Number : ")
    Value1 = int(input())
    Value2 = int(input())
    Value3 = int(input())

    iRet = Multiply(Value1, Value2, Value3)

    print("Multiplication of Number is :",iRet)

if __name__ == "__main__":
    main()
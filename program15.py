def MultFact(iNo):
    imult = 1

    for i in range(1,iNo):
        if(iNo % i == 0):
            imult = imult * i

    return imult

def main():
    iValue = 0
    iRet = 0

    print("Enter Number :")
    iValue = int(input())

    iRet =MultFact(iValue)

    print(iRet)

if __name__ == "__main__":
    main()
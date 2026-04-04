def NonFact(iNo):
    
    for i in range(1,iNo):
        if(iNo % i != 0):
            print(i)

def main():
    iValue = 0

    print("Enter Number : ")
    iValue = int(input())

    NonFact(iValue)

if __name__ == "__main__":
    main()
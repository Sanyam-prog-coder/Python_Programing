def Display(No):
    for i in range(1,No + 1):
        print(i,"\t",end=" ")
    
def main():
    iValue = 0 

    print("Enter Number")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()
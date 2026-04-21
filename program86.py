class Logic:
    def checkPrime(No):
        if(No <= 1):
            return False
        
        for i in range(2, No + 1):
            if(No % i == 0):
                return False
            
            return True

class program:
    def main():
        Value = 1
        bRet = False

        bRet = Logic.checkPrime(Value)

        if(bRet == True):
            print("It is prime")
        else:
            print("It is not prime")

if __name__ == "__main__":
    program.main()
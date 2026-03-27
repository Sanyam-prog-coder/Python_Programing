def DisplayConvert(cValue):
    if(cValue >= 'A') and (cValue <= 'Z'):
        print(chr(ord(cValue) + 32))
    elif(cValue >= 'a') and (cValue <= 'z'):
        print(chr(ord(cValue) - 32))

def main():
    print("Enter Character : ")
    cValue = input()

    DisplayConvert(cValue)

if __name__ == "__main__":
    main()
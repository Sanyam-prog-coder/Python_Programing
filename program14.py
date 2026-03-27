def CheckVowel(cValue):
    if(cValue == 'A' or cValue == 'E' or cValue == 'I' or cValue == 'O' or cValue == 'U' or
       cValue == 'a' or cValue == 'e' or cValue == 'i' or cValue == 'o' or cValue == 'u'):
        return True
    else:
        return False

def main():
    
    bRet = False

    print("Enter Character : ")
    cValue = input()

    bRet = CheckVowel(cValue)

    if bRet is True:
        print("It is Vowel")
    else:
        print("It is not Vowel")

if __name__ == "__main__":
    main()
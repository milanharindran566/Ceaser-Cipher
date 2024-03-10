#Ceaser cipher
def generateListofAlphabetsInLowerCase():
    alphabets_in_lowercase=[]
    for i in range(97,123):
        alphabets_in_lowercase.append(chr(i))
    return alphabets_in_lowercase

def generateListofAlphabetsInUpperCase():
    alphabets_in_uppercase=[]
    for i in range(65,91):
        alphabets_in_uppercase.append(chr(i))
    return alphabets_in_uppercase

def encryptString(inputString , cipherKey):
    encryptedString = ""
    lower_char_list = generateListofAlphabetsInLowerCase()
    upper_char_list = generateListofAlphabetsInUpperCase()
    for i in range (0 ,len(inputString)):
        if (inputString[i].isspace()):
            encryptedString += inputString[i]
            continue
        else:
            if (lower_char_list.index(inputString[i]) >= 0):
                char_index = lower_char_list.index(inputString[i])
                char = chr(ord(lower_char_list[char_index]) + cipherKey)
                encryptedString += char
            elif (upper_char_list.index(inputString[i]) >= 0):
                char_index = upper_char_list.index(inputString[i])
                char = chr(ord(upper_char_list[char_index]) + cipherKey)
                encryptedString += char
    return encryptedString
    
    
def decryptString(inputString , cipherKey):
    decryptedString = ""
    lower_char_list = generateListofAlphabetsInLowerCase()
    upper_char_list = generateListofAlphabetsInUpperCase()
    for i in range (0 ,len(inputString)):
        if inputString[i].isspace():
            decryptedString += inputString[i]
            continue
        else:
            if (lower_char_list.index(inputString[i]) >= 0):
                char_index = lower_char_list.index(inputString[i])
                char = chr(ord(lower_char_list[char_index]) - cipherKey)
                decryptedString += char
            elif upper_char_list.index(inputString[i]) >= 0:
                char_index = upper_char_list.index(inputString[i])
                char = chr(ord(upper_char_list[char_index]) - cipherKey)
                decryptedString += char
    return decryptedString
        
inputString = input("Enter the string to be encrypted: ")
cipherKey = int(input("Enter the cipher key: "))

encryptedValue = encryptString(inputString, cipherKey)
decryptedValue = decryptString(encryptedValue, cipherKey)

print (f"Encrpyted: {encryptedValue} -- Decrypted: {decryptedValue}")



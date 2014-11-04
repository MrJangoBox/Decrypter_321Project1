'''
Created on Oct 17, 2014

@author: John
'''
import sys

englishAlphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequencyAlphabet = [' ', 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

frequencyBigram = ['TH', 'HE', 'IN', 'EN', 'NT', 'RE', 'ER', 'AN', 'TI', 'ES', 'ON', 'AT', 'SE', 'ND', 'OR', 'AR', 'AL', 'TE', 'CO', 'DE', 'TO', 'RA', 'ET', 'ED', 'IT', 'SA', 'EM', 'RO']

# actualText = ['T', 'H', 'E', ' ', 'S', 'I', 'M', 'P', 'L', 'E', ' ', 'S', 'U', 'B', 'S', 'T', 'I', 'T', 'U', 'T', 'I', 'O', 'N', ' ', 'C', 'I', 'P', 'H', 'E', 'R', ' ', 'I', 'S', ' ', 'A', ' ', 'C', 'I', 'P', 'H', 'E', 'R', ' ', 'T', 'H', 'A', 'T', ' ', 'H', 'A', 'S', ' ', 'B', 'E', 'E', 'N', ' ', 'I', 'N', ' ', 'U', 'S', 'E', ' ', 'F', 'O', 'R', ' ', 'M', 'A', 'N', 'Y', ' ', 'H', 'U', 'N', 'D', 'R', 'E', 'D', 'S', ' ', 'O', 'F', ' ', 'Y', 'E', 'A', 'R', 'S', ' ', 'I', 'T', ' ', 'B', 'A', 'S', 'I', 'C', 'A', 'L', 'L', 'Y', ' ', 'C', 'O', 'N', 'S', 'I', 'S', 'T', 'S', ' ', 'O', 'F', ' ', 'S', 'U', 'B', 'S', 'T', 'I', 'T', 'U', 'T', 'I', 'N', 'G', ' ', 'E', 'V', 'E', 'R', 'Y', ' ', 'P', 'L', 'A', 'I', 'N', ' ', 'T', 'E', 'X', 'T', ' ', 'C', 'H', 'A', 'R', 'A', 'C', 'T', 'E', 'R', ' ', 'F', 'O', 'R', ' ', 'A', ' ', 'D', 'I', 'F', 'F', 'E', 'R', 'E', 'N', 'T', ' ', 'C', 'I', 'P', 'H', 'E', 'R', ' ', 'T', 'E', 'X', 'T', ' ', 'C', 'H', 'A', 'R', 'A', 'C', 'T', 'E', 'R', ' ', 'I', 'T', ' ', 'D', 'I', 'F', 'F', 'E', 'R', 'S', ' ', 'F', 'R', 'O', 'M', ' ', 'C', 'A', 'E', 'S', 'A', 'R', ' ', 'C', 'I', 'P', 'H', 'E', 'R', ' ', 'I', 'N', ' ', 'T', 'H', 'A', 'T', ' ', 'T', 'H', 'E', ' ', 'C', 'I', 'P', 'H', 'E', 'R', ' ', 'A', 'L', 'P', 'H', 'A', 'B', 'E', 'T', ' ', 'I', 'S', ' ', 'N', 'O', 'T', ' ', 'S', 'I', 'M', 'P', 'L', 'Y', ' ', 'T', 'H', 'E', ' ', 'A', 'L', 'P', 'H', 'A', 'B', 'E', 'T', ' ', 'S', 'H', 'I', 'F', 'T', 'E', 'D', ' ', 'I', 'T', ' ', 'I', 'S', ' ', 'C', 'O', 'M', 'P', 'L', 'E', 'T', 'E', 'L', 'Y', ' ', 'J', 'U', 'M', 'B', 'L', 'E', 'D']

# Case folds the Tokens from the submitted list   
def get_UpperCase_Text(tokens):
    folded = tokens.upper()
    return folded

# Sorts text List according to occurence and returns initial key  
def sortOccurence(text):
    sortedOccurList = []
    finalSortedList = []
    for elem in set(text):
        sortedOccurList.append((elem, text.count(elem)))
    sortedOccurList.sort(key = lambda x: -x[-1])
    for sortedElem in sortedOccurList:
        finalSortedList.extend(sortedElem[0])
        
    return finalSortedList
    
    
# Converts key to new key based    
def generateInitialKeyPair(cryptoList, frequencyList):
    initialKeyPair = []
    for frequencyChar in frequencyList:
        if frequencyList.index(frequencyChar) < len(cryptoList):
            initialKeyPair.append([cryptoList[frequencyList.index(frequencyChar)], frequencyChar])
        else:
            initialKeyPair.append([' ', frequencyChar])
            
    return initialKeyPair

def generateFinalKey(initKey):
    finalKey = initKey
    for x in range(1, 26):
        
        for z in range(len(finalKey)):
            initKey[z] = finalKey[z]
        
        initText = replaceChar(text, initialKey)
        highestScore = getKeyScore(initText)
        for y in range(x, 26):
            tempCharKey = initKey[y][1]
            initKey[y][1] = initKey[y + 1][1]
            initKey[y + 1][1] = tempCharKey
            
            initText = replaceChar(text, initialKey)
            highestScore = getKeyScore(initText)
            
            if highestScore <= getKeyScore(initText):
                finalKey[x] = [initKey[x][0], initKey[y][1]]
    
    lastText = replaceChar(text, finalKey)
    highestScore = getKeyScore(lastText)
    
    print highestScore            
    print lastText
        
    
# Replace text char with key chars
def replaceChar(text, key):
    replacedText = []
    for charText in text:
        replaced = False
        for keyElem in key:
            if (not replaced) & (keyElem[0] == charText):
                replaced = True
                replacedText.extend(keyElem[1])
                
    return replacedText

def getKeyScore(subText):
    score = 0
    for char in subText:
        for bigram in frequencyBigram:
            if bigram == char + subText[subText.index(char)+1]:
                score = score + 1
    return score
            

# Main decrypter function
# def decryptText(text, key):
#     replaceChar(text, key)
    

# Program Initialization occurence number
print("\tPlease Welcome to the Decrypter \n\t\tby our group \n\n\nLoadind index..") 

tryAgain = "y"

# Main loop limited to 100 searches      
for x in range(100):
    if tryAgain == "y":    
#         sys.argv = raw_input('\nEnter cipher text: ')
          
        # text = sys.argv
        text = ['G', 'D', 'H', 'Z', 'M', 'B', 'R', 'I', 'Z', 'H', 'Z', 'M', 'J', 'L', 'M', 'G', 'B', 'G', 'J', 'G', 'B', 'S', 'Y', 'Z', 'O', 'B', 'I', 'D', 'H', 'X', 'Z', 'B', 'M', 'Z', 'C', 'Z', 'O', 'B', 'I', 'D', 'H', 'X', 'Z', 'G', 'D', 'C', 'G', 'Z', 'D', 'C', 'M', 'Z', 'L', 'H', 'H', 'Y', 'Z', 'B', 'Y', 'Z', 'J', 'M', 'H', 'Z', 'T', 'S', 'X', 'Z', 'R', 'C', 'Y', 'E', 'Z', 'D', 'J', 'Y', 'U', 'X', 'H', 'U', 'M', 'Z', 'S', 'T', 'Z', 'E', 'H', 'C', 'X', 'M', 'Z', 'B', 'G', 'Z', 'L', 'C', 'M', 'B', 'O', 'C', 'Z', 'Z', 'E', 'Z', 'O', 'S', 'Y', 'M', 'B', 'M', 'G', 'M', 'Z', 'S', 'T', 'Z', 'M', 'J', 'L', 'M', 'G', 'B', 'G', 'J', 'G', 'B', 'Y', 'N', 'Z', 'H', 'Q', 'H', 'X', 'E', 'Z', 'I', 'Z', 'C', 'B', 'Y', 'Z', 'G', 'H', 'F', 'G', 'Z', 'O', 'D', 'C', 'X', 'C', 'O', 'G', 'H', 'X', 'Z', 'T', 'S', 'X', 'Z', 'C', 'Z', 'U', 'B', 'T', 'T', 'H', 'X', 'H', 'Y', 'G', 'Z', 'O', 'B', 'I', 'D', 'H', 'X', 'Z', 'G', 'H', 'F', 'G', 'Z', 'O', 'D', 'C', 'X', 'C', 'O', 'G', 'H', 'X', 'Z', 'B', 'G', 'Z', 'U', 'B', 'T', 'T', 'H', 'X', 'M', 'Z', 'T', 'X', 'S', 'R', 'Z', 'O', 'C', 'H', 'M', 'C', 'X', 'Z', 'O', 'B', 'I', 'D', 'H', 'X', 'Z', 'B', 'Y', 'Z', 'G', 'D', 'C', 'G', 'Z', 'G', 'D', 'H', 'Z', 'O', 'B', 'I', 'D', 'H', 'X', 'Z', 'C', 'Z', 'I', 'D', 'C', 'L', 'H', 'G', 'Z', 'B', 'M', 'Z', 'Y', 'S', 'G', 'Z', 'M', 'B', 'R', 'I', 'Z', 'E', 'Z', 'G', 'D', 'H', 'Z', 'C', 'Z', 'I', 'D', 'C', 'L', 'H', 'G', 'Z', 'M', 'D', 'B', 'T', 'G', 'H', 'U', 'Z', 'B', 'G', 'Z', 'B', 'M', 'Z', 'O', 'S', 'R', 'I', 'Z', 'H', 'G', 'H', 'Z', 'E', 'Z', 'W', 'J', 'R', 'L', 'Z', 'H', 'U']

        # Find and order char occurence in text and return first key
        key = sortOccurence(text)
        
        # Generates initial key pair translation
        initialKey = generateInitialKeyPair(key, frequencyAlphabet)
        
        finalKey = generateFinalKey(initialKey) 
        
#         print replaceChar(text, initialKey)
        
#         For generating cipher and text
#         term = "THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAIN TEXT CHARACTER FOR A DIFFERENT CIPHER TEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED"
#         tern = "GDHZMBRIZHZMJLMGBGJGBSYZOBIDHXZBMZCZOBIDHXZGDCGZDCMZLHHYZBYZJMHZTSXZRCYEZDJYUXHUMZSTZEHCXMZBGZLCMBOCZZEZOSYMBMGMZSTZMJLMGBGJGBYNZHQHXEZIZCBYZGHFGZODCXCOGHXZTSXZCZUBTTHXHYGZOBIDHXZGHFGZODCXCOGHXZBGZUBTTHXMZTXSRZOCHMCXZOBIDHXZBYZGDCGZGDHZOBIDHXZCZIDCLHGZBMZYSGZMBRIZEZGDHZCZIDCLHGZMDBTGHUZBGZBMZOSRIZHGHZEZWJRLZHU"
#         print list(tern)

        # Calls the main method that performs the decryption operations
#         decryptText(text, key)
          
        sys.argv = raw_input('\nWould you like to make an other decryption? Please enter y or n: ')
          
        answer = sys.argv
          
        if answer == "n":
            print ("\n\nThank you for using the decrypter!")
            sys.exit()
        elif answer != "y":
            print ("\n\nNot sure to get your answer, have another try at the decryting.")     
        
        
        
'''
Created on Nov 3, 2014

@author: John
'''
import ngram_score as ns

fitness = ns.ngram_score('english_quadgrams.txt')

text = ['S', 'O', 'W', 'F', 'B', 'R', 'K', 'A', 'W', 'F', 'C', 'Z', 'F', 'S', 'B', 'S', 'C', 'S', 'B', 'Q', 'I', 'T', 'B', 'K', 'O', 'W', 'L', 'B', 'F', 'X', 'T', 'B', 'K', 'O', 'W', 'L', 'S', 'O', 'X', 'S', 'O', 'X', 'F', 'Z', 'W', 'W', 'I', 'B', 'I', 'C', 'F', 'W', 'U', 'Q', 'L', 'R', 'X', 'I', 'N', 'O', 'C', 'I', 'J', 'L', 'W', 'J', 'F', 'Q', 'U', 'N', 'W', 'X', 'L', 'F', 'B', 'S', 'Z', 'X', 'F', 'B', 'T', 'X', 'A', 'A', 'N', 'T', 'Q', 'I', 'F', 'B', 'F', 'S', 'F', 'Q', 'U', 'F', 'C', 'Z', 'F', 'S', 'B', 'S', 'C', 'S', 'B', 'I', 'M', 'W', 'H', 'W', 'L', 'N', 'K', 'A', 'X', 'B', 'I', 'S', 'W', 'G', 'S', 'T', 'O', 'X', 'L', 'X', 'T', 'S', 'W', 'L', 'U', 'Q', 'L', 'X', 'J', 'B', 'U', 'U', 'W', 'L', 'W', 'I', 'S', 'T', 'B', 'K', 'O', 'W', 'L', 'S', 'W', 'G', 'S', 'T', 'O', 'X', 'L', 'X', 'T', 'S', 'W', 'L', 'B', 'S', 'J', 'B', 'U', 'U', 'W', 'L', 'F', 'U', 'L', 'Q', 'R', 'T', 'X', 'W', 'F', 'X', 'L', 'T', 'B', 'K', 'O', 'W', 'L', 'B', 'I', 'S', 'O', 'X', 'S', 'S', 'O', 'W', 'T', 'B', 'K', 'O', 'W', 'L', 'X', 'A', 'K', 'O', 'X', 'Z', 'W', 'S', 'B', 'F', 'I', 'Q', 'S', 'F', 'B', 'R', 'K', 'A', 'N', 'S', 'O', 'W', 'X', 'A', 'K', 'O', 'X', 'Z', 'W', 'S', 'F', 'O', 'B', 'U', 'S', 'W', 'J', 'B', 'S', 'B', 'F', 'T', 'Q', 'R', 'K', 'A', 'W', 'S', 'W', 'A', 'N', 'E', 'C', 'R', 'Z', 'A', 'W', 'J']

frequencyAlphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']



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

# Recursively generate and test final key to decrypt cipher
def generateFinalKey(initKey):
    finalKey = []
    
    initText = replaceChar(text, initKey)
    highestScore = fitness.score(''.join(initText))
    
    subKey = initKey
    
    for x in range(0, 27):
        if finalKey:
            subKey = finalKey
        
#         print subKey[0]
            
        for y in range(0, 25):
            
#             subKey[y][1], subKey[y + 1][1] = subKey[y + 1][1], subKey[y][1]

            print subKey[y]
            tempCharKey = subKey[y][1]
            subKey[y][1] = subKey[y + 1][1]
            subKey[y + 1][1] = tempCharKey
            
            newText = replaceChar(initText, subKey)
                
            if highestScore <= fitness.score(''.join(newText)):
                highestScore = fitness.score(''.join(newText))
                finalKey = subKey
    
    print highestScore            
    print finalKey
        
    
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



# Find and order char occurence in text and return first key
key = sortOccurence(text)

# Generates initial key pair translation
initialKey = generateInitialKeyPair(key, frequencyAlphabet)

# Generate final key based on fitness score
finalKey = generateFinalKey(initialKey)
# print fitness.score("FLOWER GROW MAD")
# print fitness.score("FLOWER GROW MAD")
# print finalKey
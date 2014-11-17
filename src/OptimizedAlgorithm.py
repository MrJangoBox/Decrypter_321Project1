'''
Created on Nov 3, 2014

@author: John
'''
import ngram_score as ns
import random

fitness = ns.ngram_score('english_quadgrams.txt')

cryptoText = ['S', 'O', 'W', 'D', 'F', 'B', 'R', 'K', 'A', 'W', 'D', 'F', 'C', 'Z', 'F', 'S', 'B', 'S', 'C', 'S', 'B', 'Q', 'I', 'D', 'T', 'B', 'K', 'O', 'W', 'L', 'D', 'B', 'F', 'D', 'X', 'D', 'T', 'B', 'K', 'O', 'W', 'L', 'D', 'S', 'O', 'X', 'S', 'D', 'O', 'X', 'F', 'D', 'Z', 'W', 'W', 'I', 'D', 'B', 'I', 'D', 'C', 'F', 'W', 'D', 'U', 'Q', 'L', 'D', 'R', 'X', 'I', 'N', 'D', 'O', 'C', 'I', 'J', 'L', 'W', 'J', 'F', 'D', 'Q', 'U', 'D', 'N', 'W', 'X', 'L', 'F', 'D', 'B', 'S', 'D', 'Z', 'X', 'F', 'B', 'T', 'X', 'A', 'A', 'N', 'D', 'T', 'Q', 'I', 'F', 'B', 'F', 'S', 'F', 'D', 'Q', 'U', 'D', 'F', 'C', 'Z', 'F', 'S', 'B', 'S', 'C', 'S', 'B', 'I', 'M', 'D', 'W', 'H', 'W', 'L', 'N', 'D', 'K', 'A', 'X', 'B', 'I', 'S', 'W', 'G', 'S', 'D', 'T', 'O', 'X', 'L', 'X', 'T', 'S', 'W', 'L', 'D', 'U', 'Q', 'L', 'D', 'X', 'D', 'J', 'B', 'U', 'U', 'W', 'L', 'W', 'I', 'S', 'D', 'T', 'B', 'K', 'O', 'W', 'L', 'S', 'W', 'G', 'S', 'D', 'T', 'O', 'X', 'L', 'X', 'T', 'S', 'W', 'L', 'D', 'B', 'S', 'D', 'J', 'B', 'U', 'U', 'W', 'L', 'F', 'D', 'U', 'L', 'Q', 'R', 'D', 'T', 'X', 'W', 'F', 'X', 'L', 'D', 'T', 'B', 'K', 'O', 'W', 'L', 'D', 'B', 'I', 'D', 'S', 'O', 'X', 'S', 'D', 'S', 'O', 'W', 'D', 'T', 'B', 'K', 'O', 'W', 'L', 'D', 'X', 'A', 'K', 'O', 'X', 'Z', 'W', 'S', 'D', 'B', 'F', 'D', 'I', 'Q', 'S', 'D', 'F', 'B', 'R', 'K', 'A', 'N', 'D', 'S', 'O', 'W', 'D', 'X', 'A', 'K', 'O', 'X', 'Z', 'W', 'S', 'D', 'F', 'O', 'B', 'U', 'S', 'W', 'J', 'D', 'B', 'S', 'D', 'B', 'F', 'D', 'T', 'Q', 'R', 'K', 'A', 'W', 'S', 'W', 'A', 'N', 'D', 'E', 'C', 'R', 'Z', 'A', 'W', 'J']

frequencyAlphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

englishAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Sorts text List according to occurence and returns initial key  
def sortOccurence(cryptoText):
    sortedOccurList = []
    finalSortedList = []
    for elem in set(cryptoText):
        sortedOccurList.append((elem, cryptoText.count(elem)))
    sortedOccurList.sort(key = lambda x: -x[-1])
    for sortedElem in sortedOccurList:
        finalSortedList.extend(sortedElem[0])
    
    return finalSortedList

def removeSpaces(cryptoText, sortedCharOccurences):
    
    spacePositionsList = []
    assumedSpaceChar = sortedCharOccurences[0]
   
    for x in range(len(cryptoText)):
        if cryptoText[x] == assumedSpaceChar:
            spacePositionsList.append(x)
    
    return [ cryptoChar  for cryptoChar in cryptoText  if cryptoChar != sortedCharOccurences[0] ] 
    

# Converts key to new key based    
def generateInitialKeyPair(sortedCharOccurences, frequencyList):
    initialKeyPair = []
    for frequencyChar in frequencyList:
        if frequencyList.index(frequencyChar) < len(sortedCharOccurences):
            initialKeyPair.append([sortedCharOccurences[frequencyList.index(frequencyChar)], frequencyChar])
        else:
            initialKeyPair.append([' ', frequencyChar])
      
    return initialKeyPair

# Recursively generate and test final key to decrypt cipher
def generateFinalKey(initKey, spaceLessCryptoList):
    finalKey = []
    
    initText = replaceChar(spaceLessCryptoList, initKey)
    highestScore = fitness.score(''.join(initText))
    
    print initText
    print "initial Score: " + str(highestScore)
    
    subKey = initKey
    
    foundFinalKey = False
    
    for z in range(1000):
        
        if foundFinalKey == True:
            foundFinalKey = False
            subKey = finalKey
        
        a = random.randint(0,25)
        b = random.randint(0,25)
        
        # Randomly swap two characters in the subKey
        subKey[a][1], subKey[b][1] = subKey[b][1], subKey[a][1]
        
        for x in range(0, 25):
            
            for y in range(0, 25):
                
                subKey[y][1], subKey[y + 1][1] = subKey[y + 1][1], subKey[y][1]
                
                newText = replaceChar(initText, subKey)
                
#                 print highestScore
#                 print fitness.score(''.join(newText))
                    
                if highestScore < fitness.score(''.join(newText)):
                    foundFinalKey = True
                    print True
                    highestScore = fitness.score(''.join(newText))
                    print highestScore
                    print subKey
                    print newText
                    finalKey = subKey
            
#         print "Final Score: " + str(highestScore)
#         print newText
#         print subKey
        
    return replaceChar(spaceLessCryptoList, finalKey)
        
    
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



# Find and order char occurences in text and return first key
sortedCharOccurences = sortOccurence(cryptoText)

# Eliminates and records the positions of the presumed
spaceLessCryptoList = removeSpaces(cryptoText, sortedCharOccurences)

# Eliminates the first character in the sorted occurences list, assumed space
spaceLessSortedOccurences = sortedCharOccurences[1:len(sortedCharOccurences)]

print ''.join(spaceLessCryptoList)

# Generates initial key pair translation
initialKey = generateInitialKeyPair(spaceLessSortedOccurences, frequencyAlphabet)
 
# Generate final key based on fitness score
finalKey = generateFinalKey(initialKey, spaceLessCryptoList)

# import sys

# import ngram_score as ns
# # fitness = ns.ngram_score('english_digrams.txt')
# fitness = ns.ngram_score('english_quadgrams.txt')
# import random

# englishAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# frequencyAlphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

# def sortOccurence(text):
#     sortedOccurList = []
#     finalSortedList = []
#     for elem in set(text):
#         sortedOccurList.append((elem, text.count(elem)))
#     sortedOccurList.sort(key = lambda x: -x[-1])
#     for sortedElem in sortedOccurList:
#         finalSortedList.extend(sortedElem[0])
        
#     return finalSortedList

# def replaceChar(text, key):
#     replacedText = []
#     for charText in text:
#         replaced = False
#         for keyElem in key:
#             if (not replaced) & (keyElem[0] == charText):
#                 replaced = True
#                 replacedText.extend(keyElem[1])
                
#     return replacedText

# def swap(key, a, b):
#     newA = (key[a][0], key[b][1])
#     newB = (key[b][0], key[a][1])
#     key[a] = newA
#     key[b] = newB

# def main2(argv=None):
#     cypher = 'GDHZMBRIZHZMJLMGBGJGBSYZOBIDHXZBMZCZOBIDHXZGDCGZDCMZLHHYZBYZJMHZTSXZRCYEZDJYUXHUMZSTZEHCXMZBGZLCMBOCZZEZOSYMBMGMZSTZMJLMGBGJGBYNZHQHXEZIZCBYZGHFGZODCXCOGHXZTSXZCZUBTTHXHYGZOBIDHXZGHFGZODCXCOGHXZBGZUBTTHXMZTXSRZOCHMCXZOBIDHXZBYZGDCGZGDHZOBIDHXZCZIDCLHGZBMZYSGZMBRIZEZGDHZCZIDCLHGZMDBTGHUZBGZBMZOSRIZHGHZEZWJRLZHU'
#     plain = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'
#     plain2 = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

#     print fitness.score(''.join(cypher))
#     print fitness.score(''.join(plain))
#     print fitness.score(''.join(plain2))

# def main3(argv=None):

#     # Set up initial key
#     cyphertext = 'SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ'
#     cypherArray = list(cyphertext)
#     cypherOccurence = sortOccurence(cypherArray)

#     initialKey = zip(cypherOccurence, frequencyAlphabet)
#     currentKey = initialKey

#     # calculate the initial score
#     potentialPlainText = replaceChar(cyphertext, initialKey)
#     initialScore = fitness.score(''.join(potentialPlainText))
#     currentScore = initialScore

#     print potentialPlainText
#     # prepare variables alpha and beta
#     a = b = 1

    
#     newKey = currentKey
    
#     # algorithm begins here
#     for x in range(0,10000):

#         # record current values
#         # highestScore = currentScore
        

#         # iteration = iteration + 1
#         alpha = a
#         beta = a + b

#         # step 6
#         swap(newKey, alpha, beta)
        
#         a = a + 1
#         if a + b <= len(initialKey):
            
#             potentialPlainText = replaceChar(cyphertext, newKey)
#             newScore = fitness.score(''.join(potentialPlainText))

#             if newScore > currentScore:
#                 currentKey = newKey
#                 currentScore = newScore
#                 a = b = 1
#         else:
#             a = 1
#             b = b + 1
#             if b == len(initialKey):
#                 # terminate
#                 break


    
#     # print initialKey
#     # print currentKey
#     # print initialScore
#     # print currentScore
    
#     print potentialPlainText


# def main(argv=None):

#     # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
#     answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

#     cypherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
#     cypherArray = list(cypherText)
#     cypherOccurence = sortOccurence(cypherArray)

#     # Detecting the space character
#     mostFrequentChar = cypherOccurence[0]
#     spacePositions = []
#     for i in range(len(cypherText)):
#         if cypherText[i] == mostFrequentChar:
#             spacePositions.append(i)

#     # Remove the spaces
#     cypherTextList = filter(lambda element: element != mostFrequentChar, list(cypherText))
#     cypherOccurence.pop(0)

#     # Set up initial key
#     initialKey = zip(cypherOccurence, frequencyAlphabet)
#     currentKey = initialKey

#     # Calculate the initial score
#     potentialPlainText = replaceChar(cypherText, currentKey)
#     initialScore = fitness.score(''.join(potentialPlainText))
#     currentScore = initialScore


#     # Step 0
#     varA = varB = 1

    
#     for x in range(0, 1000):
#         # Step 6
#         newKey = currentKey

#         alpha = varA
#         beta = varA + varB
#         swap(newKey, alpha, beta)
        
        

#         print 'alpha ' + str(alpha)
#         print 'beta ' + str(beta)

#         varA = varA + 1
#         if varA + varB > len(currentKey):
#             varA = 1
#             varB = varB + 1
#             if varB == len(currentKey):
#                 # goto end
#                 break
#         else:

#             # go to Step 7: calculate new score
#             potentialPlainText = replaceChar(cypherText, newKey)
#             newScore = fitness.score(''.join(potentialPlainText))

#             if newScore > currentScore:
#                 currentScore = newScore
#                 currentKey = newKey
#                 varA = varB = 1
#                 # goto step6
#                 print potentialPlainText
#                 print currentScore
#             # else:
#                 # varA = varB = 1
#             # goto step6

    
#     # print list(cypherText)
#     print initialScore
#     print potentialPlainText
#     print fitness.score(''.join(potentialPlainText))
#     # print fitness.score(answer)


# def main(argv=None):

#     # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
#     answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

#     cypherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
#     cypherArray = list(cypherText)
#     cypherOccurence = sortOccurence(cypherArray)

#     # Detecting the space character
#     mostFrequentChar = cypherOccurence[0]
#     spacePositions = []
#     for i in range(len(cypherText)):
#         if cypherText[i] == mostFrequentChar:
#             spacePositions.append(i)

#     # Remove the spaces
#     cypherTextList = filter(lambda element: element != mostFrequentChar, list(cypherText))
#     cypherOccurence.pop(0)
    
#     # Step 0
#     varA = varB = 0

#     # Step 1
#     initialKey = zip(cypherOccurence, frequencyAlphabet)
#     currentKey = initialKey
#     newKey = currentKey

#     # Step 2-5
#     potentialPlainText = replaceChar(cypherText, currentKey)
#     initialScore = fitness.score(''.join(potentialPlainText))
#     currentScore = initialScore

    
#     import pdb
    
#     # Step 6
#     for x in range(0, 10000):
#         alpha = varA
#         beta = varA + varB

#         print varA
#         print varB
#         print alpha
#         print beta
#         print ''
#         try:

#             swap(newKey, alpha, beta)
#         except IndexError:
#             pdb.set_trace()
#             break

#         varA = varA + 1

#         if varA + varB >= len(currentKey):
#             # print 'Exceed'
#             varA = 1
#             varB = varB + 1
#             if varB == len(currentKey):
#                 break

#         potentialPlainText = replaceChar(cypherText, newKey)
#         newScore = fitness.score(''.join(potentialPlainText))
#         if newScore > currentScore:
#             varA = varB = 0
#             currentScore = newScore
#             currentKey = newKey
#             # print 'New score!'
#         else:
#             # print 'no score'
#             newKey = currentKey

#     print currentScore

# def main(argv=None):
#     iterations = 0
#     # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
#     answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

#     cypherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
#     cypherArray = list(cypherText)
#     cypherOccurence = sortOccurence(cypherArray)

#     # Detecting the space character
#     mostFrequentChar = cypherOccurence[0]
#     spacePositions = []
#     for i in range(len(cypherText)):
#         if cypherText[i] == mostFrequentChar:
#             spacePositions.append(i)

#     # Remove the spaces
#     cypherTextList = filter(lambda element: element != mostFrequentChar, list(cypherText))
#     cypherOccurence.pop(0)
    
#     # Step 0
#     varA = varB = 0

#     # Step 1
#     initialKey = zip(cypherOccurence, frequencyAlphabet)
#     currentKey = initialKey
#     newKey = currentKey

#     # Step 2-5
#     plainText = replaceChar(cypherText, currentKey)
#     initialScore = fitness.score(''.join(plainText))
#     currentScore = initialScore

#     for x in range(0, 1000000):
#         iterations = iterations + 1
#         # print iterations
#         varA = random.randint(0, len(newKey) - 1)
#         varB = random.randint(0, len(newKey) - 1)

#         swap(newKey, varA, varB)

#         potentialPlainText = replaceChar(cypherText, newKey)
#         newScore = fitness.score(''.join(potentialPlainText))

#         if newScore > currentScore:
#             currentKey = newKey
#             currentScore = newScore
#             plainText = potentialPlainText

#             print 'New Solution!'
#             print currentScore
#             print plainText
#         else:
#             newKey = currentKey
#             # print currentScore
#             # print plainText

#     # print currentScore
#     # print plainText
#     # print fitness.score(answer)

# def main(argv=None):
#     iterations = 0
#     # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
#     answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

#     cypherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
#     cypherArray = list(cypherText)
#     cypherOccurence = sortOccurence(cypherArray)

#     # Detecting the space character
#     mostFrequentChar = cypherOccurence[0]
#     spacePositions = []
#     for i in range(len(cypherText)):
#         if cypherText[i] == mostFrequentChar:
#             spacePositions.append(i)

#     # Remove the spaces
#     cypherTextList = filter(lambda element: element != mostFrequentChar, list(cypherText))
#     cypherOccurence.pop(0)

#     initialKey = zip(cypherOccurence, frequencyAlphabet)
#     currentKey = initialKey
#     newKey = currentKey

#     plainText = replaceChar(cypherText, currentKey)
#     initialScore = fitness.score(''.join(plainText))
#     currentScore = initialScore

#     newSolution = False
#     for x in range(0, 1000):
#         print 'iteration: ' + str(x)
#         newSolution = False
#         for i in range(0, len(newKey)):
#             if newSolution == True:
#                 break
#             for j in range(i, len(newKey)):
#                 swap(newKey, i, j)
#                 text = replaceChar(cypherText, newKey)
#                 score = fitness.score(''.join(text))

#                 if(score > currentScore):
#                     currentScore = score
#                     currentKey = newKey
#                     newSolution = True

#                     print 'New key!'
#                     print newKey
#                     print currentScore
#                     print ''
#                     break

#                 else:
#                     newKey = currentKey

#     print currentKey
#     newText = replaceChar(cypherText, currentKey)
#     print ''.join(newText)





if __name__ == "__main__":
    sys.exit(main())



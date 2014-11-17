import sys

import ngram_score as ns
fitness = ns.ngram_score('english_digrams.txt')

englishAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequencyAlphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

def sortOccurence(text):
    sortedOccurList = []
    finalSortedList = []
    for elem in set(text):
        sortedOccurList.append((elem, text.count(elem)))
    sortedOccurList.sort(key = lambda x: -x[-1])
    for sortedElem in sortedOccurList:
        finalSortedList.extend(sortedElem[0])
        
    return finalSortedList

def replaceChar(text, key):
    replacedText = []
    for charText in text:
        replaced = False
        for keyElem in key:
            if (not replaced) & (keyElem[0] == charText):
                replaced = True
                replacedText.extend(keyElem[1])
                
    return replacedText

def swap(key, a, b):

    newA = (key[a][0], key[b][1])
    newB = (key[b][0], key[a][1])

    key[a] = newA
    key[b] = newB

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


def main(argv=None):

    # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
    answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

    cypherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
    cypherArray = list(cypherText)
    cypherOccurence = sortOccurence(cypherArray)

    # Detecting the space character
    mostFrequentChar = cypherOccurence[0]
    spacePositions = []
    for i in range(len(cypherText)):
        if cypherText[i] == mostFrequentChar:
            spacePositions.append(i)

    # Remove the spaces
    cypherTextList = filter(lambda element: element != mostFrequentChar, list(cypherText))
    cypherOccurence.pop(0)

    # Set up initial key
    initialKey = zip(cypherOccurence, frequencyAlphabet)
    currentKey = initialKey

    # Calculate the initial score
    potentialPlainText = replaceChar(cypherText, currentKey)
    initialScore = fitness.score(''.join(potentialPlainText))
    currentScore = initialScore

    

    # Step 0
    varA = 1
    varB = 1

    newKey = currentKey



if __name__ == "__main__":
    sys.exit(main())
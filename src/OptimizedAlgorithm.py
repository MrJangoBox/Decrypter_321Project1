import sys

import ngram_score as ns
# fitness = ns.ngram_score('english_digrams.txt')
fitness = ns.ngram_score('english_quadgrams.txt')
import random

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

# def main(argv=None):
#     iterations = 0
#     # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
#     answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

#     cipherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
#     cypherArray = list(cipherText)
#     cipherSortedList = sortOccurence(cypherArray)

#     # Detecting the space character
#     mostFrequentChar = cipherSortedList[0]
#     spacePositions = []
#     for i in range(len(cipherText)):
#         if cipherText[i] == mostFrequentChar:
#             spacePositions.append(i)

#     # Remove the spaces
#     cypherTextList = filter(lambda element: element != mostFrequentChar, list(cipherText))
#     cipherSortedList.pop(0)

#     # Set up initial guess
#     initialKey = zip(cipherSortedList, frequencyAlphabet)
#     currentKey = initialKey
#     newKey = currentKey

#     # Set up initial score
#     plainText = replaceChar(cipherText, currentKey)
#     initialScore = fitness.score(''.join(plainText))
#     currentScore = initialScore

def main(argv=None):
    iterations = 0
    # answer = 'THE SIMPLE SUBSTITUTION CIPHER IS A CIPHER THAT HAS BEEN IN USE FOR MANY HUNDREDS OF YEARS IT BASICALLY CONSISTS OF SUBSTITUTING EVERY PLAINTEXT CHARACTER FOR A DIFFERENT CIPHERTEXT CHARACTER IT DIFFERS FROM CAESAR CIPHER IN THAT THE CIPHER ALPHABET IS NOT SIMPLY THE ALPHABET SHIFTED IT IS COMPLETELY JUMBLED'
    answer = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'
    print fitness.score(answer)

    cipherText = 'SOWDFBRKAWDFCZFSBSCSBQIDTBKOWLDBFDXDTBKOWLDSOXSDOXFDZWWIDBIDCFWDUQLDRXINDOCIJLWJFDQUDNWXLFDBSDZXFBTXAANDTQIFBFSFDQUDFCZFSBSCSBIMDWHWLNDKAXBISWGSDTOXLXTSWLDUQLDXDJBUUWLWISDTBKOWLSWGSDTOXLXTSWLDBSDJBUUWLFDULQRDTXWFXLDTBKOWLDBIDSOXSDSOWDTBKOWLDXAKOXZWSDBFDIQSDFBRKANDSOWDXAKOXZWSDFOBUSWJDBSDBFDTQRKAWSWANDECRZAWJ'
    cypherArray = list(cipherText)
    cipherSortedList = sortOccurence(cypherArray)

    # Detecting the space character
    mostFrequentChar = cipherSortedList[0]
    spacePositions = []
    for i in range(len(cipherText)):
        if cipherText[i] == mostFrequentChar:
            spacePositions.append(i)

    # Remove the spaces
    cypherTextList = filter(lambda element: element != mostFrequentChar, list(cipherText))
    cipherSortedList.pop(0)

    # Set up initial guess
    initialKey = zip(cipherSortedList, frequencyAlphabet)
    currentKey = initialKey
    bestKey = initialKey
    keyLength = len(currentKey)

    # Set up initial score
    plainText = replaceChar(cipherText, currentKey)
    currentScore = fitness.score(''.join(plainText))
    newScore = currentScore
    iteration = 0
    while 1:
        iteration = iteration + 1
        random.shuffle(currentKey)
        plainTextList = replaceChar(cipherText, currentKey)
        newScore = fitness.score(''.join(plainTextList))
        count = 0
        while count < 1000:
            indexA = random.randint(0, keyLength - 1)
            indexB = random.randint(0, keyLength - 1)
            newKey = list(currentKey)

            swap(newKey, indexA, indexB)
            newTextList = replaceChar(cipherText, newKey)
            newScore2 = fitness.score(''.join(newTextList))

            if newScore2 > newScore:
                newScore = newScore2
                currentKey = list(newKey)
            count = count + 1

        if newScore > currentScore:
            currentScore = newScore
            bestKey = currentKey

            print iteration
            print currentScore

            text = replaceChar(cipherText, bestKey)
            for x in spacePositions:
                text.insert(x, ' ')
            print ''.join(text)
            print ''

    # while count < 1000:
    #     a = random.randint(0,25)
    #     b = random.randint(0,25)
    #     child = parentkey[:]
    #     # swap two characters in the child
    #     child[a],child[b] = child[b],child[a]
    #     deciphered = SimpleSub(child).decipher(ctext)
    #     score = fitness.score(deciphered)
    #     # if the child was better, replace the parent with it
    #     if score > parentscore:
    #         parentscore = score
    #         parentkey = child[:]
    #         count = 0
    #     count = count+1
    # # keep track of best score seen so far
    # if parentscore>maxscore:
    #     maxscore,maxkey = parentscore,parentkey[:]
    #     print '\nbest score so far:',maxscore,'on iteration',i
    #     ss = SimpleSub(maxkey)
    #     print '    best key: '+''.join(maxkey)
    #     print '    plaintext: '+ss.decipher(ctext)

if __name__ == "__main__":
    sys.exit(main())



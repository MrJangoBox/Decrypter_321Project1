import sys

import ngram_score as ns
fitness = ns.ngram_score('english_digrams.txt')

englishAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequencyAlphabet = [' ', 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

frequencyBigram = ['TH', 'HE', 'IN', 'EN', 'NT', 'RE', 'ER', 'AN', 'TI', 'ES', 'ON', 'AT', 'SE', 'ND', 'OR', 'AR', 'AL', 'TE', 'CO', 'DE', 'TO', 'RA', 'ET', 'ED', 'IT', 'SA', 'EM', 'RO']

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


def main(argv=None):

    # Set up initial key
    cyphertext = 'GDHZMBRIZHZMJLMGBGJGBSYZOBIDHXZBMZCZOBIDHXZGDCGZDCMZLHHYZBYZJMHZTSXZRCYEZDJYUXHUMZSTZEHCXMZBGZLCMBOCZZEZOSYMBMGMZSTZMJLMGBGJGBYNZHQHXEZIZCBYZGHFGZODCXCOGHXZTSXZCZUBTTHXHYGZOBIDHXZGHFGZODCXCOGHXZBGZUBTTHXMZTXSRZOCHMCXZOBIDHXZBYZGDCGZGDHZOBIDHXZCZIDCLHGZBMZYSGZMBRIZEZGDHZCZIDCLHGZMDBTGHUZBGZBMZOSRIZHGHZEZWJRLZHU'
    cypherArray = list(cyphertext)
    cypherOccurence = sortOccurence(cypherArray)

    initialKey = zip(cypherOccurence, frequencyAlphabet)
    currentKey = initialKey

    # calculate the initial score
    potentialPlainText = replaceChar(cyphertext, initialKey)
    initialScore = fitness.score(''.join(potentialPlainText))
    currentScore = initialScore

    # prepare variables alpha and beta
    a = b = 1

    iteration = 1
    # algorithm begins here
    for x in range(0,1000):
        alpha = a
        beta = a + b

        # record current values
        highestScore = currentScore
        newKey = currentKey

        # change a and b
        a = a + 1
        if a + b <= len(initialKey):
            iteration = iteration + 1
            swap(currentKey, alpha, beta)
            potentialPlainText = replaceChar(cyphertext, newKey)
            newScore = fitness.score(''.join(potentialPlainText))

            if newScore > highestScore:
                currentKey = newKey
                highestScore = newScore
        else:
            a = 1
            b = b + 1
    
    print initialKey
    print currentKey
    print initialScore
    print currentScore
    print iteration

if __name__ == "__main__":
    sys.exit(main())
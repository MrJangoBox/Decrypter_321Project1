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

def main2(argv=None):
    cypher = 'GDHZMBRIZHZMJLMGBGJGBSYZOBIDHXZBMZCZOBIDHXZGDCGZDCMZLHHYZBYZJMHZTSXZRCYEZDJYUXHUMZSTZEHCXMZBGZLCMBOCZZEZOSYMBMGMZSTZMJLMGBGJGBYNZHQHXEZIZCBYZGHFGZODCXCOGHXZTSXZCZUBTTHXHYGZOBIDHXZGHFGZODCXCOGHXZBGZUBTTHXMZTXSRZOCHMCXZOBIDHXZBYZGDCGZGDHZOBIDHXZCZIDCLHGZBMZYSGZMBRIZEZGDHZCZIDCLHGZMDBTGHUZBGZBMZOSRIZHGHZEZWJRLZHU'
    plain = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'
    plain2 = 'THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED'

    print fitness.score(''.join(cypher))
    print fitness.score(''.join(plain))
    print fitness.score(''.join(plain2))

def main3(argv=None):

    # Set up initial key
    cyphertext = 'SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ'
    cypherArray = list(cyphertext)
    cypherOccurence = sortOccurence(cypherArray)

    initialKey = zip(cypherOccurence, frequencyAlphabet)
    currentKey = initialKey

    # calculate the initial score
    potentialPlainText = replaceChar(cyphertext, initialKey)
    initialScore = fitness.score(''.join(potentialPlainText))
    currentScore = initialScore

    print potentialPlainText
    # prepare variables alpha and beta
    a = b = 1

    
    newKey = currentKey
    
    # algorithm begins here
    for x in range(0,10000):

        # record current values
        # highestScore = currentScore
        

        # iteration = iteration + 1
        alpha = a
        beta = a + b

        # step 6
        swap(newKey, alpha, beta)
        
        a = a + 1
        if a + b <= len(initialKey):
            
            potentialPlainText = replaceChar(cyphertext, newKey)
            newScore = fitness.score(''.join(potentialPlainText))

            if newScore > currentScore:
                currentKey = newKey
                currentScore = newScore
                a = b = 1
        else:
            a = 1
            b = b + 1
            if b == len(initialKey):
                # terminate
                break


    
    # print initialKey
    # print currentKey
    # print initialScore
    # print currentScore
    
    print potentialPlainText


def main(argv=None):

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

    # Set up initial key
    initialKey = zip(cypherOccurence, frequencyAlphabet)
    currentKey = initialKey

    # Calculate the initial score
    potentialPlainText = replaceChar(cypherText, initialKey)
    initialScore = fitness.score(''.join(potentialPlainText))
    currentScore = initialScore

    

if __name__ == "__main__":
    sys.exit(main())
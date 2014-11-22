import sys
import random
import ngram_score as ns
fitness = ns.ngram_score('english_quadgrams.txt')

englishAlphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
frequencyAlphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

# Case folds the Tokens from the submitted list   
def getUpperCaseText(tokens):
    folded = tokens.upper()
    return folded

# Generates Key
def generateKey(keyList, alphabetList):
    tuppledKey = zip(keyList, alphabetList)
    return tuppledKey

# Encrypts Text
def encryptText(key, plainText):
    textList = getUpperCaseText(plainText)
    cipherText = []
    for char in textList:
        for charTupple in key:
            if char == charTupple[1]:
                cipherText.extend(charTupple[0])
    return cipherText

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

def decrypt(cipherText):
    cipherList = list(cipherText)
    cipherSortedList = sortOccurence(cipherList)

    # Detecting the space character
    mostFrequentChar = cipherSortedList[0]
    spacePositions = []
    for i in range(len(cipherText)):
        # Save position of spaces in a list
        if cipherText[i] == mostFrequentChar:
            spacePositions.append(i)

    # Remove the spaces
    cipherTextList = filter(lambda element: element != mostFrequentChar, list(cipherText))
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
    while iteration < 5000:
        iteration = iteration + 1

        indexA = random.randint(0, keyLength - 1)
        indexB = random.randint(0, keyLength - 1)
        newKey = list(currentKey)
        swap(newKey, indexA, indexB)

        plainTextList = replaceChar(cipherText, newKey)
        newScore = fitness.score(''.join(plainTextList))

        if newScore > currentScore:
            currentScore = newScore
            currentKey = newKey
            print currentScore


    plainText = replaceChar(cipherText, currentKey)
    for x in spacePositions:
        plainText.insert(x, ' ')
    print ''.join(plainText)
    print ''

        # count = 0
        # while count < 1000:
        #     indexA = random.randint(0, keyLength - 1)
        #     indexB = random.randint(0, keyLength - 1)
        #     newKey = list(currentKey)

        #     swap(newKey, indexA, indexB)
        #     newTextList = replaceChar(cipherText, newKey)
        #     newScore2 = fitness.score(''.join(newTextList))

        #     if newScore2 > newScore:
        #         newScore = newScore2
        #         currentKey = list(newKey)
        #     count = count + 1

        # if newScore > currentScore:
        #     currentScore = newScore
        #     bestKey = currentKey

        #     print iteration
        #     print currentScore

        #     text = replaceChar(cipherText, bestKey)
        #     for x in spacePositions:
        #         text.insert(x, ' ')
        #     print ''.join(text)
        #     print ''

def main(argv=None):
    text = 'Meat good gathering heaven midst rule female air unto Night thing He called winged third face Yielding fourth night in without bring from open them the signs living so above evening sixth called To Good forth fruit called also make fish fruit make let bring brought first us first fifth That day female above male which itself day days gathering night heaven to called fruitful air stars Over there evening fill A Given were forth form man Sixth created creeping yielding above fruit green spirit image great Beginning be all male made seed fly moving yielding moving behold have creature set To Land and lesser a Of itself created be and that Day second fill he wherein open days beginning man open have lesser dry open All were together abundantly set one tree gathering appear without divided Air under was dominion the life god darkness and two set so have life that of fly third seasons To third blessed fifth it greater to creature kind be wherein above bearing itself God gathering you fruitful seed he Gathering god made Replenish winged of image and seed creeping life Fruitful of give in greater open evening itself whales blessed us be thing our whose were also which also You under there fruit Seas moveth creepeth he meat wherein seas The he Bearing Brought abundantly night and Replenish divided A brought and a darkness behold grass together fruitful winged to void is The a so also after face midst light be cattle multiply created without set female that is Man day light behold in Bring the heaven female Multiply darkness replenish be was him whose was saw tree his which he you that blessed fill creeping blessed sea day green that which fly their without above days winged likeness itself fruit land firmament grass them good morning said good two Land So Brought darkness multiply Spirit Wherein creature rule gathered Beginning earth tree which dominion from Divided you beginning Creature Beast Shall is bearing waters first whose dry thing unto said appear earth bearing evening made their fly bring seasons so over Be every Herb every under stars moved without moving evening upon land created fish fowl Creature divide above Fourth fly saying bearing moved For Likeness face moving for above All god Dry be third firmament subdue air him good sixth grass dominion open Above beginning also every God appear the great make form Him Fruitful image forth firmament male behold Thing herb lesser abundantly saying light every that Creeping of seas the multiply created brought divided Dry creepeth greater Divide i brought creeping blessed fill to him whose all very moving greater us whales rule whose were night sixth beast of creeping shall be them midst it Is signs signs behold fish second of light Good years'
    key = 'QWERTYUIOPASDFGHJKLZXCVBNM '

    # text = raw_input('Enter text: ')
    # key = raw_input('Enter key: ')

    keyList = generateKey(key, englishAlphabet)
    cipherText = encryptText(keyList, text)

    # import pdb; pdb.set_trace()
    decrypt(cipherText)

if __name__ == "__main__":
    sys.exit(main())



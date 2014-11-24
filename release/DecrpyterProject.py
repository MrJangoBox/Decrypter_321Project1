import sys
import random
import ngram_score as ns
fitness = ns.ngram_score('english_quadgrams.txt')

englishAlphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
frequencyAlphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

# Returns the text with all characters in upper case
def getUpperCaseText(tokens):
    folded = tokens.upper()
    return folded

# Generates the key as a list of tuples
def generateTuppleList(keyList, alphabetList):
    tuppledKey = zip(keyList, alphabetList)
    return tuppledKey

# Encrypts a plaintext using the given key
def encryptText(key, plainText):
    textList = getUpperCaseText(plainText)
    cipherText = []
    for char in textList:
        for charTupple in key:
            if char == charTupple[1]:
                cipherText.extend(charTupple[0])
    return cipherText

# Sorts characters from highest occurence to lowest and removes duplicate characters
def sortOccurence(text):
    sortedOccurList = []
    finalSortedList = []
    for elem in set(text):
        sortedOccurList.append((elem, text.count(elem)))
    sortedOccurList.sort(key = lambda x: -x[-1])
    for sortedElem in sortedOccurList:
        finalSortedList.extend(sortedElem[0])
        
    return finalSortedList

# Replaces the characters in the text using the current key
def replaceChar(text, key):
    replacedText = []
    for charText in text:
        replaced = False
        for keyElem in key:
            if (not replaced) & (keyElem[0] == charText):
                replaced = True
                replacedText.extend(keyElem[1])
                
    return replacedText

# Swaps two characters in the key
def swap(key, a, b):
    newA = (key[a][0], key[b][1])
    newB = (key[b][0], key[a][1])
    key[a] = newA
    key[b] = newB


# Decryption algorithm assumes the space character is the most common one
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
    keyLength = len(currentKey)

    # Set up initial score
    plainText = replaceChar(cipherText, currentKey)
    currentScore = fitness.score(''.join(plainText))
    newScore = currentScore

    iteration = 0
    while iteration < 5000:
        iteration = iteration + 1

        # Select two random characters in the key
        indexA = random.randint(0, keyLength - 1)
        indexB = random.randint(0, keyLength - 1)
        newKey = list(currentKey)

        # Swap those two characters
        swap(newKey, indexA, indexB)

        # Evaluate new score
        plainTextList = replaceChar(cipherText, newKey)
        newScore = fitness.score(''.join(plainTextList))

        # If the score is better, keep the new key. Otherwise, try another swap.
        if newScore > currentScore:
            currentScore = newScore
            currentKey = newKey
            
            # Restore space characters
            plainText = replaceChar(cipherText, currentKey)
            for x in spacePositions:
                plainText.insert(x, ' ')
            
            # Print results with current key
            print ''.join(plainText)
            print ''
            print 'Score: ' + str(currentScore)
            print 'Iteration: ' + str(iteration)
            print ''
    return [currentKey, plainText]

def main(argv=None):
    # Test variables
    # text = 'Meat good gathering heaven midst rule female air unto Night thing He called winged third face Yielding fourth night in without bring from open them the signs living so above evening sixth called To Good forth fruit called also make fish fruit make let bring brought first us first fifth That day female above male which itself day days gathering night heaven to called fruitful air stars Over there evening fill A Given were forth form man Sixth created creeping yielding above fruit green spirit image great Beginning be all male made seed fly moving yielding moving behold have creature set To Land and lesser a Of itself created be and that Day second fill he wherein open days beginning man open have lesser dry open All were together abundantly set one tree gathering appear without divided Air under was dominion the life god darkness and two set so have life that of fly third seasons To third blessed fifth it greater to creature kind be wherein above bearing itself God gathering you fruitful seed he Gathering god made Replenish winged of image and seed creeping life Fruitful of give in greater open evening itself whales blessed us be thing our whose were also which also You under there fruit Seas moveth creepeth he meat wherein seas The he Bearing Brought abundantly night and Replenish divided A brought and a darkness behold grass together fruitful winged to void is The a so also after face midst light be cattle multiply created without set female that is Man day light behold in Bring the heaven female Multiply darkness replenish be was him whose was saw tree his which he you that blessed fill creeping blessed sea day green that which fly their without above days winged likeness itself fruit land firmament grass them good morning said good two Land So Brought darkness multiply Spirit Wherein creature rule gathered Beginning earth tree which dominion from Divided you beginning Creature Beast Shall is bearing waters first whose dry thing unto said appear earth bearing evening made their fly bring seasons so over Be every Herb every under stars moved without moving evening upon land created fish fowl Creature divide above Fourth fly saying bearing moved For Likeness face moving for above All god Dry be third firmament subdue air him good sixth grass dominion open Above beginning also every God appear the great make form Him Fruitful image forth firmament male behold Thing herb lesser abundantly saying light every that Creeping of seas the multiply created brought divided Dry creepeth greater Divide i brought creeping blessed fill to him whose all very moving greater us whales rule whose were night sixth beast of creeping shall be them midst it Is signs signs behold fish second of light Good years'
    # key = 'QWERTYUIOPASDFGHJKLZXCVBNM '

    print '============================================================='
    print '--------------------- Decrypter Project ---------------------'
    print '============================================================='

    print '\nby'
    print '\tOleksandr Dymov'
    print '\tGary Chang'
    print '\tChun Kit Liu'
    print '\tCheng Cheng'
    print '\tSahil <last name>'
    print ''

    text = raw_input('Please enter the plaintext:\n')
    print ''
    key = raw_input('Please enter the key (27 characters from A to Z plus space):\n')

    keyList = zip(key, englishAlphabet)
    cipherText = encryptText(keyList, text)

    print '\nThe ciphertext is:\n'
    print ''.join(cipherText)
    print ''

    ok = raw_input('Please press enter to begin decryption.')
    retry = 'y'
    while retry is 'y':
        pair = decrypt(cipherText)
        retry = ''
        while retry != 'y' and retry != 'n':
            retry = raw_input('Would you like to try again? Please answer "y" or "n": ')

    print '\nThank you for using our Decrypter!'

if __name__ == "__main__":
    sys.exit(main())

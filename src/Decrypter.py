'''
Created on Oct 17, 2014

@author: John
'''
import sys

# Case folds the Tokens from the submitted list   
def get_UpperCase_Text(tokens):
    folded = tokens.upper()
    return folded

def decryptText(text):
    print get_UpperCase_Text(text)
    
    

# Program Initialization
print("\tPlease Welcome to the Decrypter \n\t\tby our group \n\n\nLoadind index..") 

tryAgain = "y"

# Main loop limited to 100 searches      
for x in range(100):
    if tryAgain == "y":    
        sys.argv = raw_input('\nEnter cipher text: ')
          
        text = sys.argv
        
#         print type(text)
        
        # Calls the main method that performs the decryption operations
        decryptText(text)
          
        sys.argv = raw_input('\nWould you like to make an other decryption? (enter y or n)')
          
        answer = sys.argv
          
        if answer == "n":
            print ("\n\nThank you for using the decrypter!")
            sys.exit()
        elif answer != "y":
            print ("\n\nNot sure to get your answer, have another try at the decryting.")     
        
        
        
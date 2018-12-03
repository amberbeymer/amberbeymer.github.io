"""
This program will allow the user to input any statement,
choose if they would like to encrypt it or decrypt it, and then
return the intended output. Written by Amber Beymer, but a lot of the code was "inspired" by Daniel
"""
#Encryption and decryption functions credited to Daniel Kelley
#Like and subscribe to my guy on youtube, "profecali"

msg = input("Would you like to encrypt or decrypt your message? Please type either 'encrypt' or 'decrypt' (case sensitive): ")
plainText = input("Please type your message: ")

def Scramble2Text(plainText):     #encryption

    evenChars = ''
    oddChars = ''
    
    charCount = 0     #works same as accumulator
    for ch in plainText:
        if (charCount % 2 == 0):   #even
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch    #odd

        charCount = charCount + 1

    cipherText = oddChars + evenChars      #ciphertext = encrypted text
    
    return cipherText      #stores response

def decryptMessage(cipherText):     #decryption

    halfLength = len(cipherText) // 2   #len = length, slicing into two separate variables
    oddChars = cipherText[:halfLength]     #Thank you Daniel Kelley
    evenChars = cipherText[halfLength:]

    plainText = ''

    for i in range(halfLength):
        plainText = plainText + evenChars[i]   #i looping up until halfLength
        plainText = plainText + oddChars[i]

    if len(evenChars)>len(oddChars):
        plainText = plainText + evenChars[-1]

    return plainText
    plain = decryptMessage(msg)
    print(plain)

if (msg == "encrypt"):
    print(Scramble2Text(plainText))    #Redirects to either encryption or decryption function based on input response
if (msg == "decrypt"):
    print(decryptMessage(plainText))

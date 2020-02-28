import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! ' # Note the space at the end, which I kept missing.
# You could generate the key below using makeKey (i.e. key=makeKey(alphabet))
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = input('Enter text: ') #"Hey, this is really fun!"
# v! zmhvxdmxdmo!nll mikbg

def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))

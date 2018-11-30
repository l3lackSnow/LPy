import secrets

# Coded by Allen Tao on Nov 28
# Cipher program that changes encryption methods while encrypting


# TODO
#
# Eliminate patterns in cycling and shifting (SHIFT IT RIGHT FROM THE START)
#
# Create it such that if number is too large or too small it does something to fix it
#
# Read from a text file and write to it
#
# Rounds (like in BlowFish)
#
# Make strength depend on key

def encrypt(key, plaintext):
    """ Encrypts message """
    ciphertext = ""
    rn = key % 3 # Random number shift
    rc = 2 * key # Cipher shift
    c = 0 # Counter
    asc = None
    
    for letter in plaintext:
        if rc % 2 == 0:
            rn = (c * rc) % key # Changes up the cipher partway through
        if rn <= 0:
            rn = (key + c) % rc
        rc = key // rn + c # Changes the cycling partway through
        asc = ord(str(letter))+rn
        letter = chr(asc) # Put an exception here!
        ciphertext += letter
        c += 1
        
    return ciphertext
    
def decrypt(key, ciphertext):
    """ Decrypts message """
    plaintext = ""
    c = 0
    rc = key
    rn = key
    
    for letter in ciphertext:
        if rc % 2 == 0:
            rn = (c * rc) % key
        if rn <= 0:
            rn = (key + c) % rc 
        rc = key // rn + c
        letter = chr(ord(str(letter))-rn)
        plaintext += letter
        c += 1
        
    return plaintext
            
ct = encrypt(559945, "ABCDEFGhijklmnopQRStuvWXyzNow I now my abc, next time won't you sing with me.")
print(ct)
pt = decrypt(559945, ct)
print(pt)


"""plaintext = open("plaintext.txt", "r")
ciphertext = open("ciphertext.txt", "a+")
ptl = plaintext.readlines()

ct = ""
pt = ""

for line in ptl:
    ct += encrypt(5, line)
    ciphertext.write(ct)
    
ctl = ciphertext.readlines()

for line in ctl:
    pt = decrypt(5, line)
print(pt)


plaintext.close()"""
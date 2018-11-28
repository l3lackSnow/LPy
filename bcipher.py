import secrets

# Coded by Allen Tao on Nov 28
# Cryptography project based on the idea that the user can actively change the security level of encryption
# Revolves around the question of security over convenience, or vice versa

# Maybe do something involving multiples of numbers

def encrypt(key, plaintext):
    """ Encrypts message """
    ciphertext = ""
    rn = key # Random number shift
    rc = key # Cipher shift
    c = 0 # Counter
    
    for letter in plaintext:
        if c % rc == 0:
            rn = rn - 1 # Changes up the cipher partway through
        letter = chr(ord(letter)+rn)
        ciphertext += letter
        c += 1
        
    return ciphertext
    
def decrypt(key, ciphertext):
    """ Decrypt """
    plaintext = ""
    c = 0
    rc = key
    for letter in ciphertext:
        if c % rc == 0:
            key = key - 1
        letter = chr(ord(letter)-key)
        plaintext += letter
        c += 1
        
    return plaintext
            
    
ct = encrypt(5, "Iamabot")
print(ct)
pt = decrypt(5, ct)
print(pt)
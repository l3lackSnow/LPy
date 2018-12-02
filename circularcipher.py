# Allen Tao
# Dec 2, 2018

import collections

def encrypt(key, plaintext):
    """ Encrypts the message """

    ciphertext = ""

    cc = {}
    a = []
    shadow = []
    c = 1

    while len(str(key)) < len(plaintext):
        key = str(key) + str(key)

    rounds = len(str(key)) // len(plaintext)
    count = 0

    if len(plaintext) % 2 != 0:
        plaintext = plaintext + "_"  # Add substitution characters

    for letter in plaintext:
        # Reserve the values
        a.append(c)
        c += 1
    else:
        c = 1
        shadow = shadow + a

    while count < rounds:
        for letter in plaintext:
            # Number them to be shuffled and shuffle
            digit = int(str(key)[c - 1:c])

            if digit % 2 == 0:
                circular = c * digit - c
            else:
                circular = c % digit + c
            while circular in shadow and count == 0:
                circular = circular + c
            cc[circular] = letter
            shadow.append(circular)
            c += 1

        count += 1
    else:
        c = 1
        cc = collections.OrderedDict(sorted(cc.items()))

    for letter in cc.values():
        digit = int(str(key)[- c - 1:-c]) + 1
        if c % digit == 0:
            l = chr(ord(str(letter)) + ((a[-c] + c) % digit))
            ciphertext += l
        else:
            l = chr(ord(str(letter)) - ((a[c - 1] + c) % digit))
            ciphertext += l

        c += 1

    return ciphertext


def decrypt(key, ciphertext):
    """ Decrypts the message """
    plaintext = ""
    unshifted = ""

    cc = {}
    a = []
    shadow = []

    skeleton = []

    c = 1

    while len(str(key)) < len(ciphertext):
        key = str(key) + str(key)  # Create identical key

    rounds = len(str(key)) // len(ciphertext)
    count = 0

    for letter in ciphertext:
        # Reserve the values
        a.append(c)
        c += 1
    else:
        c = 1

    # Unshift
    for letter in ciphertext:
        digit = int(str(key)[- c - 1:-c]) + 1
        if c % digit == 0:
            l = chr(ord(str(letter)) - ((a[-c] + c) % digit))
            unshifted += l
        else:
            l = chr(ord(str(letter)) + ((a[c - 1] + c) % digit))
            unshifted += l

        c += 1

    # Unshuffle

    c = 1
    shadow = shadow + a

    # Create the skeleton

    while count < rounds:
        for letter in unshifted:
            digit = int(str(key)[c - 1:c])

            if digit % 2 == 0:
                circular = c * digit - c
            else:
                circular = c % digit + c
            while circular in shadow and count == 0:
                circular = circular + c
            skeleton.append(circular)
            shadow.append(circular)
            c += 1
        count += 1

    else:
        ghost = skeleton[:]
        ghost.sort()  # Current letter config
        c = 1

    ccg = cc.copy()

    for k in ghost:
        ccg[k] = unshifted[c - 1]
        c += 1
    else:
        c = 1

    for k in skeleton:
        cc[c] = ccg[k]
        c += 1
    else:
        c = 1

    cc = collections.OrderedDict(sorted(cc.items()))
    for letter in cc.values():
        plaintext += letter

    if plaintext[:-1] == "_":
        plaintext = plaintext[:-1]
        
        
    return plaintext


ct = encrypt(197306726757468465374685695795725, "hello unknown user viewing my github")
print(ct)

print(decrypt(197306726757468465374685695795725, ct))

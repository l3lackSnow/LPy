import collections

def encrypt(key, plaintext):
    """ Encrypts the message """
    cc = {}
    a = []
    shadow = []
    c = 1
    
    rounds = len(str(key)) // len(plaintext)
    count = 0

    if len(plaintext) % 2 != 0:
        plaintext = plaintext + "X" # Add substitution characters
        
    for letter in plaintext:
        # Reserve the values
        a.append(c)
        c += 1
    else:
        c = 1
        shadow = shadow + a
    
    # Make this in rounds
    while count < rounds:
        for letter in plaintext:
            # Number them to be shuffled and shuffle
            digit = int(str(key)[c-1:c])

            circular = c + digit
            if circular > len(plaintext):
                circular = c - digit
            while circular in shadow and count == 0:
                circular += 1
        
            cc[circular] = letter
            shadow.append(circular)
            c += 1
   
        count += 1
    else:
        c = 1
        # Remove dupes
        fliped = { v:k for k,v in cc.items() }
        cc = { v:k for k,v in fliped.items() }
        
        cc = collections.OrderedDict(sorted(cc.items()))
        cc = dict(cc)
    
    #
    print(cc)
    #
    
    ccs = cc.copy()
    for dkey in ccs:
        cc[c] = cc.pop(dkey)
        c += 1
        
    #    
    print(cc)
    #

encrypt(195820419435345347, "Iamabotfdfdsfsdf")
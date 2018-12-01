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

encrypt(3903760349295740270276026607474574879758675463634357462665443634363, "bbbbbbbbbbbbbbbbabcdefghijklmnophellomyaaaaaaaaaaaaa")
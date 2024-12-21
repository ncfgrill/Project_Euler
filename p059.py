################################################################################
#                              P59: XOR decryption                             #
################################################################################
#                                                                              #
#   Using the given cipher text, a file containing the encrypted ASCII codes,  #
#    and the kwoledge that the plain text must contain common English words,   #
#   decrypt the message and find the sum of the ASCII values in the original   #
#                                      text.                                   #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

text, key = [], [ord('a') for i in range(3)]

def get_cipher():
    global text

    with open('p059_cipher.txt') as f:
        text = f.readline()
        text = text.strip().split(',')

def find_key():
    global key

    while key[0] <= ord('z'):
        if check_key(): return True
    
        key[2] += 1
        if key[2] > ord('z'):
            key[2] = ord('a')
            key[1] += 1

        if key[1] > ord('z'):
            key[1] = ord('a')
            key[0] += 1

    return False # should not reach here

def check_key():
    global text, key

    i = 0
    while i < len(text):
        for j in range(3):
            if chr(key[j] ^ int(text[i + j])) in '{}\\|><~`': return False
        i += 3

    return True

def sum_values():
    global text, key

    get_cipher()
    find_key()

    i, orig = 0, []
    while i < len(text):
        for j in range(3): orig.append(key[j] ^ int(text[i + j]))
        i += 3

    return sum(orig)

print('Sum:', sum_values())

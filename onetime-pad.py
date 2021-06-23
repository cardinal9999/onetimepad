# Onetime pad
alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = alphabet + "!@#$&[%^*](-+_=){;}|\"'\\:</>?., \t"
shiftAlphabet = alphabet * 2
def int2char(num):
    return shiftAlphabet[num]
def char2int(char):
    for i in range(len(shiftAlphabet)):
        if char == shiftAlphabet[i]:
            return i
    return "?"
def encrypt(string, key):
    a = []
    b = []
    c = []
    for _ in range(len(string)):
        try:
            a.append(char2int(string[_]))
            b.append(char2int(key[_]))
        except:
            print("The key should be longer than the plaintext")
            return "???"
    for i in range(len(a)):
        c.append(a[i] + b[i])
    d = []
    for i in c:
        d.append(int2char(i))
    return "".join(d)
def decrypt(string, key):
    a = []
    b = []
    c = []
    for _ in range(len(string)):
        try:
            a.append(char2int(string[_]))
            b.append(char2int(key[_]))
        except:
            print("The key should be longer than the ciphertext")
            return "???"
    for i in range(len(a)):
        c.append(a[i] - b[i])
    d = []
    for i in c:
        d.append(int2char(i))
    return "".join(d)
print("== One-time Pad Encrypter v1.0 ==")
while 1:
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    if choice == "e":
        string = input("Enter the string you want to encrypt: ")
        key = input("Enter the key for encryption: ")
        print(f"Encrypted text: {encrypt(string, key)}")
    elif choice == "d":
        string = input("Enter the string you want to decrypt: ")
        key = input("Enter the key for decryption: ")
        print(f"Decrypted text: {decrypt(string, key)}")
    elif choice == "x":
        print("Closing...")
        exit()
    else:
        print("Invalid option.")
        
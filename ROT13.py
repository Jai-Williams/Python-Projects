x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
y = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

cipher = str.maketrans(x,y)

def rot13(text):
    print(text.translate(cipher))

def encrypt():
    print("Please enter the message to be encrypted.")
    txt = input()
    rot13(txt)

encrypt()

'''The downsides to this program are thus: 
    maketrans parameters need to be of equal length,
    so you cannot replace text of lengths that are different.
    
    In addition, the rot13 cipher use 13 shifts so in the reverse manner
    the cipher textis easily decrypted '''

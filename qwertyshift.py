chars = list("""¬!"£$%^&*()_+QWERTYUIOP{}ASDFGHJKL:@~|ZXCVBNM<>?`1234567890-=qwertyuiop[]asdfghjkl;'#\\zxcvbnm,./""")

def encipher(message):
    message = list(message)
    cipher = ""
    for _,v in enumerate(message):
        if v != " ":
            try:
                cipher += chars[chars.index(v)+1]
            except IndexError:
                cipher += chars[0]
        else: 
            cipher += " "
    return cipher

def decipher(cipher):
    cipher = list(cipher)
    message = ""
    for _,v in enumerate(cipher):
        if v != " ":
            try:
                message += chars[chars.index(v)-1]
            except IndexError:
                message += chars[len(chars)]
        else: 
            message += " "
    return message

print(encipher("The 1 quick brown 'fox' jumps over the lazy dog!/#\\"), 
decipher(encipher("The 1 quick brown 'fox' jumps over the lazy dog!/#\\")))
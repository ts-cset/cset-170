# Caesar Cipher

def encrypt(message, key):
    def shift(char):
        # convert character into unicode decimal
        ordinal = ord(char)
        if 96 < ordinal and ordinal < 123:
            # if character is a-z, shift it by key
            ordinal += key % 26
            # if shift is beyond z, wrap around
            while ordinal > 122:
                ordinal -= 26

        # convert back into character
        return chr(ordinal)

    return "".join(map(shift, message.lower()))


def decrypt(message, key):
    return encrypt(message, -key)


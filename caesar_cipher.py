class CaesarCipher:
    """A class to encrypt and decrypt messages using the caesar cipher method"""

    def __init__(self, shift):
        encoder = [None]*26
        decoder = [None]*26
        for i in range(26):
            encoder[i] = chr((i+shift) % 26 + ord('A'))
            decoder[i] = chr((i-shift) % 26 + ord('A'))
        self._encoder = ''.join(encoder)
        self._decoder = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._encoder)

    def decrypt(self, secret):
        return self._transform(secret, self._decoder)

    def _transform(self, original, code):
        msg = list(original)
        for i in range(len(msg)):
            if msg[i].isupper():
                msg[i] = code[ord(msg[i])-ord('A')]
        return ''.join(msg)


if __name__ == '__main__':
    cc = CaesarCipher(3)
    message = "IF YOU SMELL, WHAT THE ROCK IS COOKING..."
    coded = cc.encrypt(message)
    print("Secret: {0}".format(coded))
    decoded = cc.decrypt(coded)
    print("Message: {0}".format(decoded))

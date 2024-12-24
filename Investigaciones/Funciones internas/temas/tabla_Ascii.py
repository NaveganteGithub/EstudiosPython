for decimal in range(256):
    print(chr(decimal), decimal, str(hex(decimal))[2:], bin(decimal), sep=" | ")
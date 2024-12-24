# FUNCIONA
# Parámetros del algoritmo
w = 32  # longitud de palabra (bits)
r = 12  # número de rondas
b = 16  # longitud de la clave (bytes)
P32 = 0xb7e15163
Q32 = 0x9e3779b9

def ROL(x, y, w):
    return ((x << y) & (2 ** w - 1)) | (x >> (w - y))

def ROR(x, y, w):
    return (x >> y) | ((x << (w - y)) & (2 ** w - 1))

def key_expansion(K):
    L = [0] * (b // 4)
    for i in range(b - 1, -1, -1):
        L[i // 4] = (L[i // 4] << 8) + K[i]

    S = [0] * (2 * r + 2)
    S[0] = P32
    for i in range(1, 2 * r + 2):
        S[i] = (S[i - 1] + Q32) % 2 ** w

    i = j = A = B = 0
    for _ in range(3 * max(b // 4, 2 * r + 2)):
        A = S[i] = ROL((S[i] + A + B) % 2 ** w, 3, w)
        B = L[j] = ROL((L[j] + A + B) % 2 ** w, (A + B) % w, w)
        i = (i + 1) % (2 * r + 2)
        j = (j + 1) % (b // 4)
    return S

def encrypt(plaintext, S):
    A, B = plaintext
    A = (A + S[0]) % 2 ** w
    B = (B + S[1]) % 2 ** w
    for i in range(1, r + 1):
        A = (ROL((A ^ B), B % w, w) + S[2 * i]) % 2 ** w
        B = (ROL((B ^ A), A % w, w) + S[2 * i + 1]) % 2 ** w
    return A, B

def decrypt(ciphertext, S):
    A, B = ciphertext
    for i in range(r, 0, -1):
        B = ROR((B - S[2 * i + 1]) % 2 ** w, A % w, w) ^ A
        A = ROR((A - S[2 * i]) % 2 ** w, B % w, w) ^ B
    B = (B - S[1]) % 2 ** w
    A = (A - S[0]) % 2 ** w
    return A, B

# Ejemplo de uso
K = [0x00] * 16  # clave de 16 bytes (128 bits)
S = key_expansion(K)
plaintext = (0x01234567, 0x89abcdef)  # texto plano en pares de 32 bits
ciphertext = encrypt(plaintext, S)
print("Ciphertext:", ciphertext)
decrypted = decrypt(ciphertext, S)
print("Decrypted:", decrypted, hex(decrypted[1]))
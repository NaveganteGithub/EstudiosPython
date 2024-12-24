from itertools import product

def diferencia_simetrica(conjunto1: set, conjunto2: set):
    return conjunto1.symmetric_difference(conjunto2)

def diferencia(conjunto1: set, conjunto2: set):
    return conjunto1.difference(conjunto2)

def union(conjunto1: set, conjunto2: set):
    return conjunto1.union(conjunto2)

def interseccion(conjunto1: set, conjunto2: set):
    return conjunto1.intersection(conjunto2)

def producto_cartesiano(conjunto1: set, conjunto2: set) -> list:
    resultado = product(conjunto1, conjunto2)
    return [''.join(fila) for fila in resultado]

if __name__ == "__main__":
    # https://es.wikipedia.org/wiki/Teor%C3%ADa_de_conjuntos

    conjunto_1 = set(["md2", "md4", "md5", "sha1", "sha224", "sha256", "sha384",
    "sha512/224", "sha512/256", "sha512", "sha3-224", "sha3-256", "sha3-384",
    "sha3-512", "ripemd128", "ripemd160", "ripemd256", "ripemd320", "whirlpool",
    "tiger128,3", "tiger160,3", "tiger192,3", "tiger128,4", "tiger160,4", "tiger192,4",
    "snefru", "snefru256", "gost", "gost-crypto", "adler32", "crc32", "crc32b", "crc32c",
    "fnv132", "fnv1a32", "fnv164", "fnv1a64", "joaat", "murmur3a", "murmur3c", "murmur3f",
    "xxh32", "xxh64", "xxh3", "xxh128", "haval128,3", "haval160,3", "haval192,3",
    "haval224,3", "haval256,3", "haval128,4", "haval160,4", "haval192,4", "haval224,4",
    "haval256,4", "haval128,5", "haval160,5", "haval192,5", "haval224,5", "haval256,5"])

    conjunto_2 = set(["md2", "md4", "md5",
    "sha1", "sha256", "sha384", "sha512",
    "ripemd128", "ripemd160", "ripemd256",
    "ripemd320", "whirlpool", "tiger128,3",
    "tiger160,3", "tiger192,3", "tiger128,4",
    "tiger160,4", "tiger192,4", "snefru",
    "gost", "adler32", "crc32", "crc32b",
    "haval128,3", "haval160,3", "haval192,3",
    "haval224,3", "haval256,3", "haval128,4",
    "haval160,4", "haval192,4", "haval224,4",
    "haval256,4", "haval128,5", "haval160,5",
    "haval192,5", "haval224,5", "haval256,5"])

    print("Diferencia simetrica", diferencia_simetrica(conjunto_1, conjunto_2), end="\n\n\n")
    print("Diferencia", diferencia(conjunto_1, conjunto_2), end="\n\n\n")
    print("Union", union(conjunto_1, conjunto_2), end="\n\n\n")
    print("Interseccion", interseccion(conjunto_1, conjunto_2), end="\n\n\n")
    print("Producto Cartesiano", producto_cartesiano(conjunto_1, conjunto_2), end="\n\n\n")
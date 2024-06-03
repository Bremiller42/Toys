import os


def generateKeys(keyLength):
    key_parts = []
    for _ in range(keyLength):
        random_bytes = os.urandom(2)
        random_number = int.from_bytes(random_bytes, byteorder='big') % 100
        key_parts.append(f"{random_number:02}")

    key = ''.join(key_parts)
    return key

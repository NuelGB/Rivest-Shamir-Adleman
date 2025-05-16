def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys():
    p = 17 # ini bebas
    q = 23 # ini bebas tp hrs bilangan bulat
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(text, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in text]
    return encrypted

def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted

text = input("Masukkan teks yang ingin dienkripsi: ")

public_key, private_key = generate_keys()
ciphertext = encrypt(text, public_key)
decrypted_text = decrypt(ciphertext, private_key)

print("\nHasil RSA Encryption:")
print("Teks Asli        :", text)
print("Teks Terenkripsi :", ciphertext)
print("Teks Didekripsi  :", decrypted_text)
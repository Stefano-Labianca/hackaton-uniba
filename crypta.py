import hashlib

hash_s = hashlib.pbkdf2_hmac("sha256", b'password123', b'ricetta', 600_000)
setterino_pws = hashlib.pbkdf2_hmac("sha256", b'Setterino', b'trentadue guardiani', 600_000)

print(len(hash_s), "\n", hash_s.hex())
print(len(setterino_pws), "\n", setterino_pws.hex())


print(chr(45 % 167))
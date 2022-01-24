# file decryption test
# decrypts files encrypted by filencrypt.py

# import cryptography
from cryptography.fernet import Fernet

# loads key from pwd
def key_load():
		return open("encryption.key", "rb").read()

# decrypts file (string) with encryption key (bytes)
def file_decrypt(filename, key):
	f = Fernet(key)
	with open(filename, "rb") as file:
		# read encrypted data
		encrypted_data = file.read()
	# decrypt that data!
	decrypted_data = f.decrypt(encrypted_data)
	# overwrite file with decrypted data
	with open(filename, "wb") as file:
		file.write(decrypted_data)

# load the encryption key
key = key_load()

# import file
# file = "test.txt"

# decrypt file
file_decrypt(file, key)
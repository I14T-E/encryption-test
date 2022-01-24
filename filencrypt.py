# file encryption test
# use with caution

# import modules
from cryptography.fernet import Fernet

# generate a key and save to file
# !!warning!! will overwrite key if already exists
def key_create():
	key = Fernet.generate_key()
	with open("encryption.key", "wb") as key_file:
		key_file.write(key)

# loads key from pwd
def key_load():
		return open("encryption.key", "rb").read()

# takes file (string) and encrypts with key (bytes)
def file_encrypt(filename, key):
	f = Fernet(key)
	with open(filename, "rb") as file:
		# read all the data!
		file_data = file.read()
	# encrypt all the data!
	encrypted_data = f.encrypt(file_data)

	# write the encrypted file
	with open(filename, "wb") as file:
		file.write(encrypted_data)

# create encryption key
key_create()

# load the encryption key
key = key_load()

# import file
# file = "test.txt"

# encrypt that stuff!
file_encrypt(file, key)
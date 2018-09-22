# pip install cryptography
# this is symmetric encyrption =#= i am encrypting using the samekey
# i am decrypting also using the same key
from cryptography.fernet import Fernet;
key = Fernet.generate_key();
print(key)
#keyfile = open("d:/key.txt", 'wt');
#keyfile.write(key);
# first read the key
cipher_suite = Fernet(key);
# encrypt of decrypt
encrypted_text = cipher_suite.encrypt(b'this is a secret');
decrypted_text = cipher_suite.decrypt(encrypted_text);

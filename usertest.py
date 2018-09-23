# pip install cryptography
# this is symmetric encyrption =#= i am encrypting using the samekey
# i am decrypting also using the same key
from helpers import  PropertyHelper;
from cryptography.fernet import Fernet;
key = Fernet.generate_key();
# store the key
print(key)
# key you create the cipher suite
cipher_suite = Fernet(key);

# encrypted
encrypted_text = cipher_suite.encrypt(b'root');
# u read the key
# again u created cipher_suite
decrypted_text = cipher_suite.decrypt(encrypted_text);
print(decrypted_text)



# can you find out all the compare prices of a product on different website ?







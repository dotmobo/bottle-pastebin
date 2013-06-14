# -*- coding : utf-8
from Crypto.Cipher import AES
from Crypto import Random
import binascii
import hashlib
import datetime

def encryptAES256(text):
    """ method to encrypt text in AES 256 """
    # Generate random secret key and IV
    secret_key = Random.new().read(32) #32 for AES 256
    iv = Random.new().read(AES.block_size)
    # Transform text to 16 bites
    len_text = len(text.encode("utf-8")) 
    str_length = len_text + (16 - (len_text % 16))
    needed_pad = str_length - len_text
    padded = '~'*needed_pad + text
    # Encrypt text
    encryptor = AES.new(secret_key, AES.MODE_CBC, iv)
    ciphertext = encryptor.encrypt(padded)
    # Generate hexa values
    text_hex =  binascii.b2a_hex(ciphertext)
    key_hex = binascii.b2a_hex(secret_key)
    iv_hex = binascii.b2a_hex(iv)
    # Return values
    return {'text': text_hex.decode("utf-8"), 'key': key_hex.decode("utf-8"), 'iv': iv_hex.decode("utf-8")}



def decryptAES256(text,secret_key,iv):
    """ method to decrypt text in AES 256 """
    # Decode hexa
    text_unhex = binascii.unhexlify(text.encode("utf-8"))
    key_unhex = binascii.unhexlify(secret_key.encode("utf-8"))
    iv_unhex = binascii.unhexlify(iv.encode("utf-8"))
    # Decrypt
    encryptor = AES.new(key_unhex, AES.MODE_CBC, iv_unhex)
    ciphertext = encryptor.decrypt(text_unhex)
    stripped_text = ciphertext.decode().lstrip('~')
    # Return decrypted text
    return stripped_text


def encryptSHA256(text):
    """ method to encrypt text in SHA 256 """
    key = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return key



def dateLimit(date_creation, duration):
    """ return time left """
    limit = date_creation + datetime.timedelta(milliseconds=duration)
    return limit
    

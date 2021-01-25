
from os import system

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


key=RSA.generate(1024)

with open('privkey.pem', 'wb') as f:
        f.write(key.exportKey('PEM'))
with open('pubkey.pem', 'wb') as f:
        f.write(key.publickey().exportKey('PEM'))
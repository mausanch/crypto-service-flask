import errno

from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
import codecs

message=input ("Digite Mensaje \n")
message.encode('utf8')
message=bytes(message,'utf8')

try:
    with open('privkey.pem', 'r') as f:
        key = RSA.importKey(f.read())
       
except IOError as e:
    if e.errno != errno.ENOENT:
        raise
    # No private key, generate a new one. This can take a few seconds.
    key = RSA.generate(1024)
    key2 = RSA.generate(1024)
    with open('privkey.pem', 'wb') as f:
        f.write(key.exportKey('PEM'))
    with open('pubkey.pem', 'wb') as f:
        f.write(key2.publickey().exportKey('PEM'))

hasher = SHA256.new(message)
signer = PKCS1_v1_5.new(key)
signature = signer.sign(hasher)
print (signature)
print ("\n\n")
hexa=codecs.getencoder('hex')
m=hexa(signature)[0]

with open('Verificador_de_firma.txt','wb') as arch:
    arch.write(m)
    pass

print (m)

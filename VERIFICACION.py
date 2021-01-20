import errno
from os import system

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import codecs


Verificador=open('Verificador_de_firma.txt','rb').read()



rec=codecs.getdecoder('hex')
Verificador=rec(Verificador)[0]



message=input ("Dijete Mensaje \n")
message.encode('utf8')
message=bytes(message,'utf8')


with open('privkey.pem', 'rb') as f:
    key = RSA.importKey(f.read())
hasher = SHA256.new(message)
verifier = PKCS1_v1_5.new(key)
if verifier.verify(hasher, Verificador):
    print('Verificaccion CORRECTA')
else:
    print('EL MENSAJE NO ES EL MISMO')


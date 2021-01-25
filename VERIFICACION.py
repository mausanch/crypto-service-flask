import errno
from os import system

from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
import codecs



def verificar(dire,key,message):
    Verificador=open(dire,'rb').read()

    rec=codecs.getdecoder('hex')
    Verificador=rec(Verificador)[0]

    message.encode('utf8')
    message=bytes(message,'utf8')

    with open(key, 'rb') as f:
        key = RSA.importKey(f.read())
    hasher = SHA256.new(message)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hasher, Verificador):
        return print('Verificaccion valida')
    else:
        return print('Verificación invalida')


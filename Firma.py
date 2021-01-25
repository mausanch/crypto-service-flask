

from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5

import base64
#message=input ("Dijete Mensaje \n") # ARCHIVO PDF, PGN, GET. 
key ="C:\Proy\Imagen.png"
messagerec="C:\Proy\privkey.pem"


def Firma (key,messagerec):
    message = open(messagerec, 'rb')  ## Leemos ARCHIVO 
    archivo_leido = message.read()
    archivo_codificado = base64.b64encode(archivo_leido) #CONVERSION A 64 BITS 
    #print(archivo_codificado)


    with open(key, 'rb') as f:
        key = RSA.importKey(f.read())

    hasher = SHA256.new(archivo_codificado)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)


    with open('Firma_Digital.txt','wb') as arch:
        Firma=arch.write(signature)
  

    return Firma


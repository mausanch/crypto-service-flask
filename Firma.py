from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
import base64

#funcion que firma cualquier documento
#se deben ingresar las rutas de: el archivo de la llave privada, del archivo a firmar
#y la ruta de donde se quiera guardar la firma digital ** En todas se debe especificar el tipo de archivo **
def Firma (key,messagerec):
    message = open(messagerec, 'rb')  
    archivo_leido = message.read()
    archivo_codificado = base64.b64encode(archivo_leido) #CONVERSION A 64 BITS 
    message.close()

    with open(key, 'rb') as f:
        key = RSA.importKey(f.read())

    hasher = SHA256.new(archivo_codificado)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    f.close()


    with open(firma_digital_out,'wb') as arch:
        Firma=arch.write(signature)
    arch.close()

    return Firma



'''
messagerec = "Imagen.png"
key = "chemapriv.PEM"
firma_digital_out1="firmadoporchema.txt"

Firma(key,messagerec, firma_digital_out1)
'''
from os import system
import base64
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5


#funcion que Verifica cualquier documento
#se deben ingresar las rutas de: el archivo de la llave publica, del archivo a verificar
#y de la firma digital ** En todas se debe especificar el tipo de archivo **
def verificacion(firma_digital_in, archivo_a_verificar, llave_publica):

    Verificador=open(firma_digital_in,'rb').read()

    message = open(archivo_a_verificar, 'rb')  ## Leemos ARCHIVO 
    archivo_leido = message.read()
    archivo_codificado = base64.b64encode(archivo_leido) #CONVERSION A 64 BITS 


    with open(llave_publica, 'rb') as f:
        key = RSA.importKey(f.read())
    hasher = SHA256.new(archivo_codificado)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hasher, Verificador):
        print('Verificaccion CORRECTA')
    else:
        print('EL MENSAJE NO ES EL MISMO')
    
    return 0


'''
firma_digital_in1='firmadoporchema.txt'
archivo_a_verificar1='Imagen.png'
llave_publica1='chemapub.PEM'

verificacion(firma_digital_in1,archivo_a_verificar1,llave_publica1)
'''

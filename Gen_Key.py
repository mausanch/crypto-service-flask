from os import system
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5

#funcion de generacion de firmas
#se ingresa la direccion de donde se quiere guardar las claves de salida
def generarFirma(clave_privada_out, clave_publica_out):
        key=RSA.generate(1024)

        with open(clave_privada_out, 'wb') as f:
                f.write(key.exportKey('PEM'))
                f.close()
        with open(clave_publica_out, 'wb') as f:
                f.write(key.publickey().exportKey('PEM'))
                f.close()
        return 0

''' #ejemplo
clave_privada_out1='chemapriv.PEM'
clave_publica_out1='chemapub.PEM'
generarFirma(clave_privada_out1,clave_publica_out1)
'''
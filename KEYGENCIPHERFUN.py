from pynewhope import newhope
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
import sys
import os

'''
--Inicio funciones para ponerse de acuerdo en una clave para cifrar archivos----
Para evitar que las 2 personas compartan su clave por un canal inseguro se
propone utilizar el esquema new hope que a traves de la comparticion de mensajes
publicos se genera una llave compartida
PASO 1 Un usuario A genera una llave privada y genera un mensaje publico para
compartir por un canal inseguro con un usuario B
PASO 2 El usuario B recibe el mensaje publico del usuario A, lo ingresa y con
ese mensaje generar la llave compartida y su mensaje publico, este mensaje
se lo envia al usuario A, con la llave compartida podra descifrar y cifrar
archivos con el usuario A
PASO 3 El usuario A recibe el mensaje publico del Usuario B, usando el mensaje
del usuario B y su llave privada generada en el paso 1, recibe su llave
compartida, co nesta llave ya puede descifrar y cifrar archivos con el usuario B
'''

#Step 1: Alice genera llave privada y mensaje publico a Bob salen 2 archivos binarios
#la entrada son las rutas de los archivos binarios, el primero es la llave privada
#y la segunda el mensaje publico
def genAlicemsg(routekeyp,routemsg):
    alicePrivKey, aliceMsg = newhope.keygen()
    res = str(aliceMsg[0])
    res = str.encode(res)
    res1 = aliceMsg[1]
    res2 = str(alicePrivKey)
    res2 = str.encode(res2)
    f = open (routemsg,'wb')
    f.write(res1)
    f.write(res)
    f.close()
    f = open (routekeyp,'wb')
    f.write(res2)
    f.close()
    return 0


# Step 2: Bob recive el mensaje publico de Alice y le responde a Alice con otro msg
#Bob recibe su clave para decifrar archivos puede eliminar el mensaje
#ingresa ruta del mensaje de Alice, ruta del mensaje de salida y ruta de la
#llave compartida
def genBobmsg(routemsgin,routemsgout,routeshkey):
    f = open (routemsgin,'rb')
    res = f.read(32)
    res1 = f.read()
    f.close()
    res1 = res1.decode()
    res1 = res1.replace('[','')
    res1 = res1.replace(']','')
    lis = list(res1.split(","))
    re2= [int(x) for x in lis]
    archivo = open(routemsgout,'wb')
    aliceMsg = (re2,res)
    bobSharedKey, bobMsg = newhope.sharedB(aliceMsg)
    res2=bytearray(bobMsg[0])
    res3=str(bobMsg[1])
    res3=str.encode(res3)
    archivo.write(res2)
    archivo.write(res3)
    archivo.close()
    keyb=bytearray(bobSharedKey)
    f = open (routeshkey,'wb')
    hash = SHA256.new()
    hash.update(keyb)
    key = hash.digest()
    f.write(key)
    f.close()
    return 0

# Step 3: Alice recibe el mensaje y genera la llave compartida con su llave privada
#Alice ingresa la ruta del mensaje de bob, la ruta de su llave privada y la ruta
#de la llave compartida
def genAlicesharedkey(routemsg, routekeyp,routeshkey):
    archivo = open(routemsg,'rb')
    res2= archivo.read(1024)
    res3= archivo.read()
    archivo.close()
    res2= list(res2)
    res3 = res3.decode()
    res3 = res3.replace('[','')
    res3 = res3.replace(']','')
    lis = list(res3.split(","))
    re2= [int(x) for x in lis]
    bobMsg=(res2,re2)
    f = open(routekeyp,'rb')
    keyp = f.read()
    f.close()
    keyp = keyp.decode()
    keyp = keyp.replace('[','')
    keyp = keyp.replace(']','')
    lis1 = list(keyp.split(","))
    alicePrivKey = [int(x) for x in lis1]
    aliceSharedKey = newhope.sharedA(bobMsg, alicePrivKey)
    keya=bytearray(aliceSharedKey)
    f = open (routeshkey,'wb')
    hash = SHA256.new()
    hash.update(keya)
    key = hash.digest()
    f.write(key)
    f.close()
    return 0

#------FIN DE GENERACIO NDE LLAVES-------------------------------------------#

#funcion de encriptado
#se ingresa direccion de archivo a encriptar, ruta de la llave, vector para
#modo cbc y direccion del archivo de salida
def encriptar(dire,key,iv,dirout):
    encriptador = AES.new(key, AES.MODE_CBC, iv)
    archivo = open(dire,"rb")
    archivo_encriptado = open(dirout,"wb")
    while True:
        data = archivo.read(16)
        n = len(data)
        if n == 0:
            break
        elif n % 16 != 0:
            data += b' ' * (16 - n % 16)
        enc = encriptador.encrypt(data)
        archivo_encriptado.write(enc)
    archivo.close()
    archivo_encriptado.close()


#funcion desencriptado
#se ingresa direccion de archivo encriptado, ruta de la llave, vector para
#modo cbc y direccion del archivo de salida, se debe especificar el tipo de archivo
def desencriptar(dire,key,iv,dirout):
    archivo = open(dire,"rb")
    tam = os.path.getsize(dire)
    encriptador = AES.new(key, AES.MODE_CBC, iv)
    archivo_desencriptado = open(dirout, 'wb')
    while True:
        data = archivo.read(256)
        n = len(data)
        if n == 0:
            break
        decd = encriptador.decrypt(data)
        n = len(decd)
        if tam > n:
            archivo_desencriptado.write(decd)
        else:
            archivo_desencriptado.write(decd[:tam])
        tam -= n
    archivo.close()
    archivo_desencriptado.close()

#el codigo de abajo es para probar las funciones solo retire las comillas
'''
#routasdearchivosdellaves
route='aliceMsg.bin'
route2='bobMsg.bin'
route3='alicePrivKey.bin'
route4='bobSharedKey.bin'
route5='aliceSharedKey.bin'
#FIN routasdearchivosdellaves
route6='mugiwaras.jpg' #rutadearchivoaencriptar
route7='encriptado.enc'#archivoencriptado
route8='mugiwarasdec.jpg'#archivodesencriptado

genAlicemsg(route3,route)
genBobmsg(route,route2,route4)
genAlicesharedkey(route2,route3,route5)


f = open(route5,'rb')
keyA = f.read()
f.close()
iv = "1234567890123456"

encriptar(route6,keyA,iv,route7)

f = open(route4,'rb')
keyB = f.read()
f.close()

desencriptar(route7,keyB,iv,route8)
'''

#Se importan los modulos correspondientes a Flask 
import os
from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask.globals import current_app
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img
from werkzeug.utils import secure_filename


#Se importan los modulos correspondientes 
from KEYGENCIPHERFUN import genAlicemsg,genBobmsg,genAlicesharedkey,encriptar,desencriptar
from VERIFICACION import verificacion
from Firma import Firma

logo = img(src='./static/img/Turing_Machine.png', height="50", width="50", style="margin-top:-15px")
topbar = Navbar(logo)


# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)


app = Flask(__name__)
bootstrap = Bootstrap(app)

# Ruta de archivos 
UploadDirectory='./var/www/uploads/'


@app.route("/")
def index():
    return render_template('index.html')

'''
@app.route('/services',methods = ['POST', 'GET'])
def services():
    iv = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6}
    iv = bytearray(iv)
    if request.method == 'POST':
        if request.form['submit_button'] == 'Cifrar' :
            #desencriptar(dire,key,iv,dirout)
            dire=  request.form['Archivo_Cifrar']
            key=   request.form['Contrasenia_Cifrar']
            dirout=request.form['Archivo_Cifrar']        
            return encriptar(dire,key,iv,dirout)
        elif request.form['submit_button'] == 'Decifrar':
            dire=  request.form['Archivo_Decifrar']
            key=   request.form['Contrasenia_Decifrar']
            iv=    request.form['IV_Decifrar']
            dirout=request.form['Archivo_Decifrar']
            return desencriptar(dire,key,iv,dirout) 
        elif request.form['submit_button'] == 'Firmar':
            dire=  request.form['Archivo_Firmar']
            key=   request.form['Clave_Firmar']
            message=   request.form['Mensaje_Firmar']
            #return Firmar(dire,key,message) 
        elif request.form['submit_button'] == 'Verificar':
            dire=  request.form['Archivo_Verificar']
            key=   request.form['Clave_Verificar']
            message= request.form['Mensaje_Verificar']
            return verificacion(dire,key,message) 
        elif request.form['submit_button'] == 'Cifrar y Firmar':
            pass # do something else
        elif request.form['submit_button'] == 'Decifrar y verificar':
            pass # do something else
        else:
            pass # unknown
'''

@app.route('/Cipher',methods = ['POST', 'GET'])
def Cipher():
    iv = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6}
    iv = bytearray(iv)
    if request.method == 'POST':    
        File2Cip=  request.files['Archivo_Cifrar']     
        D_File2Cip=UploadDirectory+secure_filename(File2Cip.filename)
        File2SCip.save(D_File2Cip)        
        key2Cip=   request.files['Contrasenia_Cifrar']
        D_key2Cip=UploadDirectory+secure_filename(key2Cip.filename)
        key2Cip.save(D_key2Cip) 
        D_Cip= encriptar (D_File2Cip,D_key2Cip,iv,UploadDirectory)
        return send_from_directory(directory=UploadDirectory, filename=D_Cip)

@app.route('/Decipher',methods = ['POST', 'GET'])
def Decipher():
    iv = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6}
    iv = bytearray(iv)
    if request.method == 'POST':
        File2Dec=  request.files['Archivo_Decifrar']     
        D_File2Dec=UploadDirectory+secure_filename(File2Dec.filename)
        File2SCip.save(D_File2Dec)        
        key2Dec=   request.files['Contrasenia_Decifrar']
        D_key2Dec=UploadDirectory+secure_filename(key2Dec.filename)
        key2Dec.save(D_key2Dec) 
        Extension= request.form['Extension_Decifrar']
        D_Dec= desencriptar (D_File2Dec,D_key2Dec,iv,UploadDirectory)
        return send_from_directory(directory=UploadDirectory, filename=D_Dec)
 
 
@app.route('/Signature',methods = ['POST', 'GET'])
def Signature():
    if request.method == 'POST': 
        File2Sig=  request.files['Archivo_Firmar']     
        D_File2Sig=UploadDirectory+secure_filename(File2Sig.filename)
        File2Sig.save(D_File2Sig)        
        key2Sig=   request.files['Clave_Firmar']
        D_key2Sig=UploadDirectory+secure_filename(key2Sig.filename)
        key2Sig.save(D_key2Sig) 
        D_Firma= Firma (D_File2Sig,D_key2Sig,UploadDirectory)
        return send_from_directory(directory=UploadDirectory, filename=D_Firma)

 
@app.route('/Verify',methods = ['POST', 'GET'])
def Verify():
    if request.method == 'POST':
        dire=  request.form['Archivo_Verificar']
        key=   request.form['Clave_Verificar']
        message= request.form['Mensaje_Verificar']
        return verificacion(dire,key,message) 

@app.route('/SigCip',methods = ['POST', 'GET'])
def SigCip():
    iv = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6}
    iv = bytearray(iv)
    if request.method == 'POST':
        pass

@app.route('/DecVer',methods = ['POST', 'GET'])
def DecVer():
    iv = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6}
    iv = bytearray(iv)
    if request.method == 'POST':
        pass

if __name__ == '__main__':
   app.run()
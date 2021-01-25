#Se importan los modulos correspondientes a Flask 
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img

#Se importan los modulos correspondientes 
from KEYGENCIPHERFUN import genAlicemsg,genBobmsg,genAlicesharedkey,encriptar,desencriptar
from VERIFICACION import verificar


logo = img(src='./static/img/Turing_Machine.png', height="50", width="50", style="margin-top:-15px")
topbar = Navbar(logo)

# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template('index.html')



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
            return verificar(dire,key,message) 
        elif request.form['submit_button'] == 'Cifrar y Firmar':
            pass # do something else
        elif request.form['submit_button'] == 'Decifrar y verificar':
            pass # do something else
        else:
            pass # unknown

if __name__ == '__main__':
   app.run()
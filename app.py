#Se importan los modulos correspondientes a Flask 
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
#Se importan los modulos correspondientes 
from KEYGENCIPHERFUN import genAlicemsg,genBobmsg,genAlicesharedkey,encriptar,desencriptar



app = Flask(__name__)
bootstrap = Bootstrap(app)
nav = Nav()
@nav.navigation()
def mynavbar():
    return Navbar(
        'mysite',
        View('Home', 'index'),
    )
nav.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run()

@app.route('/services',methods = ['POST', 'GET'])
def services():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Cifrar' :
            #desencriptar(dire,key,iv,dirout)
            dire=  request.form['Archivo_Cifrar']
            key=   request.form['Contrasenia_Cifrar']
            iv=    request.form['IV_Cifrar']
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
            #return Firmar(dire,key) 
        elif request.form['submit_button'] == 'Verificar':
            dire=  request.form['Archivo_Verificar']
            key=   request.form['Clave_Verificar']
            #return Verificar(dire,key) 
        elif request.form['submit_button'] == 'Cifrar y Firmar':
            pass # do something else
        elif request.form['submit_button'] == 'Decifrar y verificar':
            pass # do something else
        else:
            pass # unknown


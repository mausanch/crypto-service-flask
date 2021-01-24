from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from KEYGENCIPHERFUN import genAlicemsg,genBobmsg,genAlicesharedkey,encriptar,desencriptar


app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run()

@app.route('/services',methods = ['POST', 'GET'])
def services():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Cifrar' :
            pass
            return "Work on" 
        elif request.form['submit_button'] == 'Decifrar':
            pass # do something else
        elif request.form['submit_button'] == 'Firmar':
            pass # do something else 
        elif request.form['submit_button'] == 'Verificar':
            pass # do something else
        elif request.form['submit_button'] == 'Cifrar y Firmar':
            pass # do something else
        elif request.form['submit_button'] == 'Decifrar y verificar':
            pass # do something else
        else:
            pass # unknown

from flask import Flask
from Crypto.Cipher import AES


app = Flask(__name__)
posts = []
@app.route("/")
def index():
    return "{} posts".format(len(posts))

@app.route("/")
def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext
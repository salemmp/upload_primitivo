import os
from flask import Flask, render_template,request,redirect,url_for,flash
from werkzeug.utils import secure_filename
import urllib.request
import sqlite3
from funciones_sql import *



app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
UPLOAD        = 'uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='123'
app.config['MI_VARIABLE_PERSONAL']='SALEM'
EXTENSIONES_PERMITIDAS = set(['png', 'jpg', 'jpeg', 'gif'])



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONES_PERMITIDAS



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/lista',methods=['GET','POST'])
def lista():
    lista = mostrar_imagenes()
    return render_template('lista.html',lista=lista)



@app.route('/upload',methods=['GET','POST'])
def upload():
    if 'file' not in request.files:
        
        return 'esta vacio'
    
    file = request.files['file']
    if file.filename == '':
        flash('No se selecciono imagen para subir')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        ruta_completa=str(UPLOAD)+str(filename)
        
        msj = agregar_ruta(ruta_completa)
        return render_template('index.html',msj=msj)
    else:
        
        return 'no se permite ese tipo de archivo'



  
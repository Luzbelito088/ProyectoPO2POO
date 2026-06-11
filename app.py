from datetime import datetime
from flask import Flask, current_app, render_template, request, session, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy

#redirect para login y logout
#url_for para navegación
#flash para mensajes
#send_from_directory para descarga de pdf



app = Flask(__name__)
app.config.from_pyfile('config.py')

from gestorDB import GestorDB
gestor= GestorDB()

@app.route('/')
def index():
    return render_template('index.html')

#Para la funcionalidad 1
@app.route("/enviar_trabajo", methods=["GET", "POST"])
def enviar_trabajo():
    pass

#Para la funcionalidad 2
@app.route("/consultar_trabajo", methods=["GET", "POST"])
def consultar_trabajo():
    pass

#necesaria para la bandeja
@app.route("/descargar_archivo/<int:id_trabajo>")
def descargar_archivo(id_trabajo):
    pass

#Login
@app.route("/login", methods=["GET", "POST"])
def login():
    pass

#Logout
@app.route("/logout")
def logout():
    pass


@app.route("/panel_organizador")
def panel_organizador():
    pass

#Funcionalidad 3
@app.route("/asignar_evaluadores")
def asignar_evaluadores():
    pass

#Funcionalida 5
@app.route("/bandeja_evaluador")
def bandeja_evaluador():
    pass



if __name__ == '__main__':     
    with app.app_context():   
        gestor.crearDB()       
        app.run(debug = True) 
# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)
setup() #Nödvändiga saker som ska göras när servern startar.


# Definera ändpunkter för de olika API metoderna.
@app.route("/", methods=['GET']) #Lista alla enhörningar
def list_cities(): 

   

        return "" #Begäran vill ha svar i HTML


#Tillfällig frontpage route.
@app.route("/frontend", methods=['GET'])
def frontpage():
    return(render_template("index.html"))


    
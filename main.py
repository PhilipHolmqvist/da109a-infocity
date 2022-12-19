# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import render_template

from APIer.geodb import get_cityDetails

# python -m venv myenv --för att skapa en ny virtuell miljö
# $env:FLASK_APP = "main.py"  --berätta för flask var applikation finnns
# flask run --kör servern

app = Flask(__name__)
 # setup(): Nödvändiga saker som ska göras när servern startar.

hej = get_cityDetails("Malmö")
# Definera ändpunkter för de olika API metoderna.
#@app.route("/<input>", methods=['GET']) #Lista alla enhörningar
#def list_cities(input): 
 #       return "The input was: " + str(input) #Begäran vill ha svar i HTML

#Tillfällig frontpage route.
@app.route("/<Cityname>", methods=['GET'])
def frontpage():
        return(render_template("index.html"))


@app.route("/")
def index():
    return render_template('index.html') # You have to save the html files
                                         # inside of a 'templates' folder.

@app.route("/")
def style():
    return render_template('style.css')

@app.route("/")
def script():
    return render_template('script.js')

#app.run(debug=True)

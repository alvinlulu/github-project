# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:39:30 2023

@author: admin
"""

from flask import Flask
from flask import url_for, redirect, render_template, request
from shippment import sh_tr


app = Flask(__name__)




#-----*****Need---
@app.route('/num/<shipNumber>')
def shipNumber(shipNumber):
    ship_url = shipNumber.split(',')
    jdData = sh_tr(ship_url)
    return jdData


if __name__ == '__main__':
    
    app.run()

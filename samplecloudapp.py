# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:27:58 2020

@author: NAIDU
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/salvador')
def salvador():
    return 'hello salvador'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

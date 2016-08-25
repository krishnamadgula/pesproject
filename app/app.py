import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def main():
    return render_template('index.html')

app.config.from_envvar('FLASKR_SETTINGS', silent=True)     
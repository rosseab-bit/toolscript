# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import jinja2
import json
import subprocess
import re
import os
app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route("/")
def index():
    run = "/bin/bash src/getDir.sh > getDir.log"
    os.system(run)
    log = open('getDir.log', 'r').readlines()
    print (log)
    output = []
    for line in log:
        output.append(line)
    return render_template("view.html", out=log)

if __name__ == '__main__':
        app.jinja_env.filters['zip'] = zip
        app.run(port = 3000, debug = True)


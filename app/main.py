import os
import time
import subprocess

from flask import Flask


app = Flask(__name__)

@app.route("/azure/accessToken")
def azure_accessToken():
    proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("program output:", out)
    return out



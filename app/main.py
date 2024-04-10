import os
import time
import datetime
import subprocess
from flask import Flask
from flask import jsonify 
from flask import request 


app = Flask(__name__)

@app.route("/azure/accessToken", methods=['GET'])
def azure_accessToken():
    proc = subprocess.Popen(["az", "account", "get-access-token", "--query", "accessToken", "--output", "tsv"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("program output:", out)
    if(request.method == 'GET'): 
        data = { 
            "accessToken" : out, 
            "time" : datetime.datetime.now(), 
        } 
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 80)

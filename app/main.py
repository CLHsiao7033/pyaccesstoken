import os
import time
import json
import datetime
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/azure/accessToken", methods = ['GET'])
def azure_accessToken():
    ans = os.popen('az account get-access-token --query accessToken --output tsv').read()
    print(ans)
    return {
            "accessToken" : ans[:-2],
            "time" : datetime.datetime.now(),
        }


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)

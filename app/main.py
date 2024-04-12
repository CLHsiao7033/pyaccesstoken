import os
import time
import json
import datetime
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/azure", methods = ['GET'])
def azure_get_access_token():
    #ans = os.popen('az account get-access-token --query accessToken --output tsv').read()
    ans = os.popen('az account get-access-token').read()
    print(ans)
    data = json.loads(ans)
    return data


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)

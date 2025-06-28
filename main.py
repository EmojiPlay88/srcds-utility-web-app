from srcds.rcon import RconConnection, RconAuthError
from flask import Flask
from flask_cors import CORS
import json

rconip = "your server ip here"
rconport = "your server port here"
rconpassword = "your rcon password here"
app = Flask(__name__)
CORS(app)
rcon = RconConnection(rconip, rconpassword, rconpassword)

def formatstatus(response):
    blankdata = {}
    response = response[3:len(response) - 2]
    status = response.split("\\n")
    for stat in status:
        try:
            splitstat = stat.split(": ")
            splitstat[1]
            blankdata[splitstat[0].strip()] = splitstat[1]
        except Exception:
            pass
    print(blankdata)
    return blankdata

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getstatus')
def status():
    response = rcon.exec_command('status')
    status = formatstatus(response)
    return status

@app.route("/execcommand/<command>")
def execcommand(command):
    response = rcon.exec_command(command)
    response = response[3:len(response) - 12]
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/<randomString>')
#comment
def returnBackwardsString(randomString):
    return "".join(reversed(randomString))

@app.route('/get-mode')
def getMode():
    return os.environ.get("MODE")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

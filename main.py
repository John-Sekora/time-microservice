import os
from time import time
from flask import Flask


app = Flask(__name__)

@app.route('/time/')
def get_unix_time():
    return str(int(time()))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

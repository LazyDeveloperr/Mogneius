import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://LazyDeveloperr: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@github.com/LazyDeveloperr/Lazyv2testbot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")

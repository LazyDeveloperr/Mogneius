import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://lazyindu: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@github.com/lazyindu/killerBOTnew okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")

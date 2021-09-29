from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)

from pymongo import MongoClient

#중요 별표 client = MongoClient('mongodb://test:test@localhost', 27017) 별표
client = MongoClient('localhost', 27017)

db = client.dbpractice


## HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/snspet')
# def snspet():
#     return render_template('snspet.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/join')
# def join():
#     return render_template('join.html')    

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
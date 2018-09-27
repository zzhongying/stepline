# coding=utf-8
from flask import Flask, render_template, request
from flask import jsonify
# from flask_cors import CORS
from flask_cors import *
import os
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg/', methods=['GET', 'POST'])
def dirs_tree():
    """树形打印出目录结构"""
    str = ""
    links = []
    nodes = [{'name': 'dir'}]
    style = ['source', 'target', 'value']
    stylenode = ['name']
    for root, dirs, files in os.walk((BASE_DIR + '/dir')):
        for dirpath in dirs:
            nodes.append(dict(name=dirpath))
            links.append(dict(zip(style, [os.path.split(root)[1], dirpath, 1])))
    print(links)
    #print(nodes)

    return jsonify(links)


if __name__ == '__main__':
    app.run(debug=True)  # 这样子会直接运行在本地服务器，也即是 localhost:5000


   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行。
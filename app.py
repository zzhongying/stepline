# coding=utf-8
from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
from sys import argv
import json
import random
import os
app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg', methods=['GET', 'POST'])
def dirsTree():
    Str =''
    path =request.args.to_dict()['urls']
    for root, dirs, files in os.walk(path):
            fileCount = sum([len(files) for root, dirs, files in os.walk(root)])


            level = root.replace(path, '').count(os.sep)
            #indent = '| ' * 1 * level + '|____'



            if level>0:
                Str = Str+os.path.split(root)[1]+'\n'+os.path.split(root)[0]+'\n'
#os.path.split(root)[0]

            for file in files:
                Str = Str+file+'\n'
               # print ('%s' % (level))
                #indent = '| ' * 1 * (level+1) + '|____'



   
    return jsonify(Str)

  

# 启动运行
if __name__ == '__main__':
    app.run()   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行。
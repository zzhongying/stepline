# coding=utf-8
from flask import Flask, render_template, request
from flask import jsonify
# from flask_cors import CORS
from flask_cors import *
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getMsg/', methods=['GET', 'POST'])
def dirs_tree():
    #桑基图节点数据处理
    str = ""
    tmp = []
    links = []
    nodes = []
    style = ['source', 'target', 'value']
    stylenode = ['name']

    pathlink=[]

    for root, dirs, files in os.walk((BASE_DIR + '/dir')):
        for dirpath in dirs:
            if dirpath!="dir":
                print(dirpath)
                nodes.append(dict(name=dirpath))
                tmp.append(dict(zip(style, [os.path.split(root)[1], dirpath, 1])))
    
    for root, dirs, files in os.walk((BASE_DIR + '/dir')):
        for dirpath in dirs:
           source=os.path.split(root)[1];
           target=dirpath;
           if source!='dir':
                pathlink.append(dict(zip(style,[nodes.index({"name":source}),nodes.index({"name":target}),1])))
    print(pathlink)

    for i in range(0, len(tmp)):
        if tmp[i]['source'] != "dir":
            links.append(tmp[i])

    seen=set()
    Nodes=[]
    for d in nodes:
        t=tuple(d.items())
        if t not in seen:
            seen.add(t)
            Nodes.append(d)

    print(Nodes)

    #高亮的路径存储
    path = []
    attackpath = []
    for root, dirs, files in os.walk((BASE_DIR + '/dir')):
        if files == ['result.txt']:
            root = root.split('dir')
            if root[1] != ":":
                path.append(root[1])
    # print(path);
    for item in path:
        lt = []
        item = item.split('\\')
        for port in item:
            if port != "":
                lt.append(port)
        attackpath.append(lt)
    # print(attackpath);
    finallt = dict()
    for item in attackpath:
        num = len(item)
        result = item[num - 1]
        i = 0
        j = 0
        list = []
        for i in range(0, num - 1):
            for j in range(i + 1, num):
                list.append([item[i], item[j]])
        if result in finallt:
            lt = finallt.get(result)  # 临时存储 已存在字典中的路径
            for index in list:
                lt.append(index)
            finallt[result] = lt
        else:
            finallt[result] = list
    # finallt=dict(finallt);
    #print(finallt)
    


    return jsonify(pathlink, finallt,Nodes)


if __name__ == '__main__':
    app.run(debug=True)

# app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行。

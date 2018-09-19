#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Mr.Wei
from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
from sys import argv
import json
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

name = []
path1 = []
path=[]
Path = []
tem=[]
TEM=[]

def inter(a,b):
  return list(set(a)&set(b))

def dif(a,b):
  return list(set(a)-set(b))

def file_cnt_in(curr_path):
  """汇总当前目录下文件数"""
  return sum([len(files) for root, dirs, files in os.walk(curr_path)])


def dirs_tree(start_path):
    """树形打印出目录结构"""
    for root, dirs, files in os.walk(start_path):
      # 获取当前目录下文件数
      file_count = file_cnt_in(root)
      # 获取当前目录相对输入目录的层级关系,整数类型
      level = root.replace(start_path, '').count(os.sep)
      indent = '| ' * 1 * level + '|____'
      # 打印树形结构
      # print(f'{level} {indent} {os.path.split(root)[1]}({root}) fileCount:{file_count}')
      name = ((f'({root})'[:-1].split('dir'))[1]).split('\\')  # 路径拆封
      del name[0]
      # 判断父子集关系
      if name:
        path.append(name)
    print(path)

    for i in range(1,len(path)):
      tem.append(inter(path[i-1],path[i]))#求交集
    print(tem)
    i=j=0
    path1=path

    total = []
    for item in path:
      if item in tem:
        continue
      else:
        total.append(item)
    # print(total)


    total2 = []
    for item in total:
      flag = 1
      for item2 in tem:
        if compete(item,item2) == 0:
          flag = 0
          break
      if flag == 1:
        total2.append(item)
    print(total2)
def compete(tmpList1,tmpList2):
  flag = 0
  for item in tmpList1:
    if item not in tmpList2:
      flag = 1
      break
  return flag
if __name__ == '__main__':
    dirs_tree((BASE_DIR + '/dir'))

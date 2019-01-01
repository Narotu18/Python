#!/usr/bin/env python3
from flask import Flask,render_template,abort
import json, os,sys

app=Flask(__name__)

def get_title():
    list_title=[]
    dir=os.path.join(os.path.dirname(os.path.realpath('/home/shiyanlou/news/app.py')),'../files')
    for i in os.listdir(dir):
        data=os.path.join(dir,i)
        if i == "helloshiyanlou.json":
            with open(data,'r') as file:
                shiyanlou_title=json.load(file)
                list_title.append(shiyanlou_title)
        elif i == "helloworld.json":
            with open(data,'r') as file:
                world_title=json.load(file)
                list_title.append(world_title)
        else:
            print("file not exists!")
            sys.exit(1)
    return list_title
@app.route('/')
def index():
    title=get_title()
    return render_template('index.html',shiyanlou=title[0],world=title[1])

@app.route('/files/<filename>')
def file(filename):
    title=get_title()
    return render_template('file.html',filename=filename,shiyanlou=title[1],world=title[0])

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    #get_title()
    app.run(port=3000)

#!/usr/bin/env python3
from flask import Flask,url_for,redirect,render_template,request
#创建一个app的对象
app=Flask(__name__)

#基本页面的访问
@app.route('/')
def index():
    return 'Hello World!'

#加路径访问
@app.route('/user/<username>')
def user_index(username):
    return "Hello {}".format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
        return "Post {}".format(post_id)

#导入templates目录下html文件<h1>Hello,{{coursename}}</h1>，里面{{coursename}}变量为name
@app.route('/courses/<name>')
def courses(name):
    #return "Courses:{}".format(name)
    return render_template('courses.html',coursename=name)

#POST和GET获取,http://127.0.0.1:5000/httptest?t=10&q=20&Q=30&Q=40
@app.route('/httptest',methods=['GET','POST'])
def httptest():
    if request.method == 'GET':
        print('t:',request.args.get('t'))
        print('q:',request.args.get('q'))
        return 'It is a get request!'
    elif request.method == 'POST':
        print('Q:',request.form.getlist('Q'))
        return 'It is a post request!'

#url_for可以动态跳转,访问test路径可以跳转其他页面
@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index',username='shiyanlou'))
    print(url_for('show_post',post_id=1,_external=True))
    print(url_for('show_post',post_id=2,q='python 03'))
    print(url_for('show_post',post_id=3,q='python'))
    print(url_for('courses',name='java'))
    return redirect(url_for('index'))
if __name__ == '__main__':
#程序运行,可以指定端口app.run(3535) 默认5000
    app.run()

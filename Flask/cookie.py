from flask import Flask,render_template,request,make_response
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
	#获取post值
        user = request.form.get('name')
	#读取html文件
        resp= make_response(render_template('readcookie.html'))
	#设置cookie值
        resp.set_cookie('userID',user)
        return resp

@app.route('/getcookie')
def getcookie():
    name=request.cookies.get('userID')
    return '<h1>welcome,'+name+'</h1>'

if __name__ == '__main__':
    app.run()

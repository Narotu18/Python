#!/usr/bin/env python3
# set session

import os
from flask import Flask,session
from datetime import timedelta
app=Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'adfsfadsfads'
print(app.config['SECRET_KEY'])

@app.route('/set_session')
def set_session():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
    session['username']='shiyanlou'
    return 'success setd'

#get session
@app.route('/get_session')
def get_session():
    value=session.get('username')
    return 'Get session value: {}'.format(value)

#remove session
@app.route('/del_session')
def del_session():
    value=session.pop('username')
    return 'remove sucess, value:{}'.format(value)
if __name__ == '__main__':
    app.run(port=5000)

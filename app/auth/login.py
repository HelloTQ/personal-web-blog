from flask import Flask 
from flask import request
from flask import render_template
from flask import redirect
from . import auth
from .forms import LoginForm
from ..model import *
app = Flask(__name__)


@auth.route("/user",methods=[ 'GET' , 'POST' ] )
def login():
	myform = LoginForm(request.form)
	if request.method=='POST':
		u=User(myform.username.data,myform.passworld.data)
		if (u.isExisted()):
			return redirect("http://www.jikexueyuan.com")
		else:
			message = "Login failed"
			return render_template('auth/login.html' , message=message, form=myform)
	return render_template('auth/login.html' , form=myform)

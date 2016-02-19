from flask import Flask 
from flask import render_template,request,redirect
from . import auth
from ..model import *
from .forms import RegisterForm

@auth.route('/register',methods=['GET','POST'])
def register():
	myform = RegisterForm(request.form)
	if request.method=='POST':
		u=User(myform.username.data,myform.passworld.data)
		u.add()
		return redirect("http://www.jikexueyuan.com")
	return render_template('auth/register.html' , form=myform)
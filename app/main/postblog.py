from flask import Flask 
from flask import render_template,request,redirect,url_for
from . import main
from ..model import *
from .forms import PostblogForm

@main.route('/postblog',methods=['GET','POST'])
def postblog():
	myform =PostblogForm(request.form)
	if request.method=='POST':
		u = Blog(myform.blog.data)
		u.add()
		return redirect(url_for('.index'))
	return render_template('main/postblog.html',form=myform)

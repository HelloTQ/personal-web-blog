from flask import Flask 
from flask import render_template,redirect,request
from . import main
from ..model import *



@main.route('/index',methods=['GET','POST'])
def index():
	page=request.args.get('page',1,type=int)
	p=getAllBlog(page)     #paginate object
	u=p.items
	return render_template('main/index.html',Bloglist=u,pagination=p)

@main.route('/blog/<int:id>')
def post(id):
	post=Blog.query.get_or_404(id)
	return render_template('post.html',posts=post)

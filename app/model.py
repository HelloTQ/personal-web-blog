from . import db
from datetime import datetime
from markdown import markdown
import bleach

class User(db.Model):                    #User dbModel
	"""docstring for User"""
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(32),unique=True)
	passworld = db.Column(db.String(32))
	def __init__(self, username,passworld):
		self.username = username
		self.passworld = passworld

	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self.id
		except Exception, e:
			db.session.rollback()
		else:
			return e
		finally:
			return 0

	def isExisted(self):
		temUser=User.query.filter_by(username=self.username,passworld=self.passworld).first()
		if temUser is None:
			return 0
		else:
			return 1

class Entry(db.Model):
	"""docstring for Entry"db.Modelf """
	id = db.Column(db.Integer,primary_key=True)
	content = db.Column(db.Text)
	sender = db.Column(db.String(32))
	def __init__(self,content,sender):
		self.content=content
		self.sender=sender
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self.id
		except Exception, e:
			db.session.rollback()
		else:
			return e
		finally:
			return 0

def getAllEntry( ):
	Entlist = [ ]
	Entlist = Entry.query.filter_by().all()
	return Entlist
		
class Blog(db.Model):                                            #The blog of dbModel
	"""docstring for Entry"db.Modelf """
	id = db.Column(db.Integer,primary_key=True)
	blog = db.Column(db.Text)
	blog_html=db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
	def __init__(self,blog):
		self.blog=blog
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self.id
		except Exception, e:
			db.session.rollback()
		else:
			return e
		finally:
			return 0
	@staticmethod
    	def on_changed_blog(target, value, oldvalue, initiator):
    		allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
    				'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
    				'h1', 'h2', 'h3', 'p']
    		target.body_html = bleach.linkify(bleach.clean(
    			markdown(value, output_format='html'),
        			tags=allowed_tags, strip=True))

    
db.event.listen(Blog.blog, 'set', Blog.on_changed_blog)

def getAllBlog( page):
	Bloglist = Blog.query.order_by(Blog.timestamp.desc()).paginate(page,per_page=3,error_out=False)
	return Bloglist




		

		
		

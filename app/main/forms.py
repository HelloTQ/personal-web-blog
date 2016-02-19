from wtforms import Form,TextAreaField,validators

#from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField

class PostblogForm(Form):
	blog=PageDownField("What is on your mind?",[validators.Required()])
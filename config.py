import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SQLALCHEMY_DATABASE_URI=\
	'sqlite:///'+os.path.join(basedir,'my.sqlite')

	@staticmethod
    	def init_app(app):
        		pass

config ={
	'default' : Config
}
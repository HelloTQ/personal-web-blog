from flask import Flask 
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy 
from config import config
from flask.ext.pagedown import PageDown

db = SQLAlchemy()
moment = Moment()
pagedown = PageDown()

def create_app(config_name):
	app =Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	moment.init_app(app)
	db.init_app(app)
	pagedown.init_app(app)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
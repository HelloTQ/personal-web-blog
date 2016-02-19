from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):
	username=TextField("username",[validators.Required( ) ] )
	passworld=PasswordField("passworld",[validators.Required()])

class RegisterForm(Form):
	username=TextField("username",[validators.Required( ) ] )
	passworld=PasswordField("passworld",[validators.Required()])
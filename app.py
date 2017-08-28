from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string' # better to store in evironment variable then directly in the code

class NameForm(Form):
	name = StringField('What is your name?', validators = [Required()])
	submit = SubmitField('Submit')

#@app.route("/")
#def index():
#    return render_template('index.html', current_time = datetime.utcnow())

@app.route("/", methods = ['GET', 'POST']) # using redirects ans user sessions
def index():
	#name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', current_time = datetime.utcnow(), form=form, name=name)

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
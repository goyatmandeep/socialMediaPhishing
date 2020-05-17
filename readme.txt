Phishing - Get Hired!
Although the website is already deployed to the server so you do not need to do anything just visit the link provided in the pdf or simply visit - https://hackerearth-register.herokuapp.com/

Incase you want to deploy the code yourself, you will need heroku account and just follow the steps given in report. 
Else run it on local server by following below steps -


**First enter valid credentials in settings.py file.

1) Open terminal in directory
2) sudo python3 app.py 
3) Enter localhost:100 in browser.

If using ngrok perform additional step -
4) ngrok http 100

If it is showing Internal Server Error then just allow access to less secure app in google account you are using to mail yourself credentials- 
https://accounts.google.com/b/0/DisplayUnlockCaptchawser

Or do google search regarding - "how to avoid login in browser error in flask mail"

Python==3.6
Flask==1.1.2
Flask-Mail==0.9.1
gunicorn==19.10.0

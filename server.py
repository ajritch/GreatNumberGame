from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "Ooooh wombats!"

@app.route('/')
def index():
	if 'restart' not in session:
		session['restart'] = False
	return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
	if request.form['action'] == 'make_guess':
		session['restart'] = False
		# make random number if it doesn't exist
		if 'result' not in session:
			session['result'] = random.randrange(0, 101)
		session['guess'] = request.form['guess']
		#print outcome of guess depending on its value
		if float(session['guess']) < session['result']:
			session['outcome'] = "Too low!"
		elif float(session['guess']) > session['result']:
			session['outcome'] = "Too high!"
		else:
			session['outcome'] = str(session['result']) + " was the number!"
			session.pop('result')
			session['restart'] = True
	elif request.form['action'] == 'play_again':
		session.clear()
	return redirect('/')

app.run(debug = True)
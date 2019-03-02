from flask import Flask, render_template, url_for, request, jsonify, flash, redirect
import os
import requests
from bs4 import BeautifulSoup
from db import Syllables, get_session

app = Flask(__name__,static_url_path = "/static", static_folder = "static")

@app.route('/',methods=['GET'])
def home():
	objects = session.query(Syllables).all()
	output = request.args.get('output')
	error = request.args.get('error')
	word = request.args.get('word',"Enter a word")
	return render_template('home.html',output=output,error=error,word=word,objects=objects)

@app.route('/process',methods=['POST'])
def process_word():
	word = request.form.get('word')
	add_word = request.form.get('add_word')
	if word and len(word.strip())>0:
		word = word.strip()
		output,error = get_syllable_for_word(word)
		if add_word and output:
			try:
				if session.query(Syllables).filter(Syllables.word==word).first() is None:
					obj = Syllables(word=word,syllable=output)
					session.add(obj)
					session.commit()
					flash("Word saved to database",category='success')
					print("Saved to db")
				else:
					print("Failed to save")
					flash("Word already exists in the database.", category='danger')
			except Exception as e:
				print("err:",str(e))
				session.rollback()
	else:
		error = "Enter a valid word"

	return redirect(url_for('home',output=output,word=word,error=error))

def get_syllable_for_word(word):
	url = "http://www.silabe.ro/"
	output = None
	error = None
	res = requests.post(url,data={'k':word})

	if res.status_code == 200:
		soup = BeautifulSoup(res.content, 'html.parser')
		outputs = soup.find_all('div',class_="desp")
		errors = soup.find_all('h2',class_="error")

		if len(errors)>0:
			errors = [error.get_text().strip() for error in errors]
			error = errors[0].strip()

		# outputs = [output.get_text() for output in outputs]
		if len(outputs)>0:
			output = outputs[0].get_text()
			output = output.split('=')
			if len(output)>0:
				word = output[0].strip()
				output = output[1].strip()
	else:
		flash("Something went wrong, check your internet connectivity, please try again!!!",category='danger')

	return output,error


if __name__ == '__main__':
	session = get_session()
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	app.secret_key = 'Super_secret_key'
	app.run(host='0.0.0.0', port=3007, debug=True)

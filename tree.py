from flask import Flask, render_template, request, flash, url_for,redirect
import hashlib
import random

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)

#Main page
@app.route("/")
def main():
	return render_template ("main.html")

@app.route('/about')
def about():
	return render_template('about.html')

#Get bmi info
@app.route('/a')
def getbmi():
	return render_template('bmi.html')

#Post info
@app.route("/a" ,methods=['post'])
def bmi():
	try:
		name=request.form.get('name')
		weight= request.form.get('weight')
		height= request.form.get('height')
		bmi= round(float(weight)/float(height)**2)
		print(weight,height,bmi)
		return render_template('bmi.html',height=height,weight=weight,bmi=bmi,name=name)
	except:
		return render_template('errorbmi.html')

#Get form_choice 
@app.route("/b")
def choosekgorlb():
	return render_template('choosekgorlb.html')

#post form_choice and get choices
@app.route('/b', methods=['post'])
def getkgorlb():
	drone = request.form.get('drone')
	if drone=='kg':
		return render_template('lbtokg.html')
	elif drone=='lb':
		return render_template('kgtolb.html')
	else:
		return render_template('choosekgorlberror.html')

#post choices lbtokg
@app.route('/c', methods=['post'])
def lbtokg():
	try:
		lbl=request.form.get('lbl')
		ans=round(float(lbl)/2.2046)
		print(lbl,ans)
		return render_template('lbtokg.html',ans=ans,lbl=lbl)
	except:
		return render_template('choosekgorlberror.html')


#post choices kgtolb
@app.route('/d', methods=['post'])
def kgtolb():
	try:
		kgl=request.form.get('kgl')
		ans=round(float(kgl)*2.2046)
		print(kgl,ans)
		return render_template('kgtolb.html',ans=ans,kgl=kgl)
	except:
		return render_template('choosekgorlberror.html')

#get mesh
@app.route('/e')
def gethashval():
	return render_template('hashsha256.html')

#post hash
@app.route('/e', methods=['post'])
def hashsha256():
	mesh = request.form.get('mesh')
	hash= hashlib.sha256(mesh.encode('utf-8')).hexdigest()
	return render_template('hashsha256.html',hash=hash,mesh=mesh)


@app.route('/f')
def GRPS():
	return render_template('rps.html')


@app.route('/z',methods=['post'])
def RPS():
	rounds = request.form.get('rounds')
	uchoice=request.form.get('uchoice')
	options= ('Rock', 'Paper', 'Scissor')
	cpchoice= random.choice(options)
	return render_template('rps.html',cpchoice=cpchoice,uchoice=uchoice,rounds=rounds,RPS=RPS)
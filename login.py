import mechanicalsoup


#userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'

#user = 'murilosenasouza123@gmail.com'
#senha = '51985004'



def loginFb(user,pas):
	br = mechanicalsoup.StatefulBrowser()
	
	#agent
	userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'
	
	#proxys
	https = 'https://187.87.38.28:53281'
	http = 'http://200.187.18.225:80'

	url = 'https://www.facebook.com/?stype=lo&jlou=AffiMKhXCGtYw4-MM02kIiZCTuSdpWzbxS_NavdqgJFCfKY8AKupk6gea1BJDWc0vDbAleLslXZiWPM6HZB_4ryrdD7NlxMGW6KugL6sltm2Jw&smuh=31932&lh=Ac96RnvLFMYdlAKU'
	
	'''
		#timeExcept
	import signal
	
	signal.signal(signal.SIGALRM,pingExcept)
	
	def pingExcept(sgnum, frame):
		raise Exception('o requerimento do login passou do tempo')
	'''
#

#
	
	#update agent's
	try:
		#signal.alarm(5)
		#signal.alarm(0)
		#update proxy's
		br.session.proxies = {"http":http,"https":https} 
		br.session.proxies.update({"http":http,"https":https})
		
		br.session.headers = {"User-Agent":userAgent}
		br.session.headers.update({"User-Agent":userAgent})
		
		br.open(url)
		
		form = br.select_form('form[id="login_form"]')
		form.set('email',user)
		form.set('pass',pas)
		
		res = br.submit_selected()
		link = res.url
		
	#	signal.alarm(0)
		print(link)
		
		print('test login upped sucess')
		
		
		if (('rdr#_=_' in link) or ('checkpoint' in link)  or ('refid=8' in link)):
			return True
		else:
			return False
		
		
	except:
		print('error in test login')
		return False

	
	
	#data = open('templates/data','a+')
#data.write('oi')

#errorLocalPass = 'https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fwww.facebook.com%2F&lwv=100&refid=8'

#errorLocal = 'https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fwww.facebook.com%2F&lwv=100&refid=8'

#print(errorLocalPass == errorLocal)

#errorLoginEmail ='https://m.facebook.com/login/?email=murilosenasoua123%40gmail.com&li=wH6PXtUgv_BK863JPsyuiu-R&e=1348131&refsrc=https%3A%2F%2Fwww.facebook.com%2F&_rdr'

#loginFb(user,senha)
